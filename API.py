from flask import Flask
from flask_restful import Api, Resource

import csv
import json

app = Flask(__name__)
api = Api(app)


class Menu(Resource):
    def get(self):
        with open('./menu.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        pizzas = []
        toppings = []
        drinks = []

        for row in contents:
            if row[1] == 'pizza':
                pizzas.append(row)

            elif row[1] == 'topping':
                toppings.append(row)

            elif row[1] == 'drink':
                drinks.append(row)

        return {'pizzas': pizzas, 'toppings': toppings, 'drinks': drinks}


class ItemPrice(Resource):
    def get(self, item_id):
        price_index = 4
        with open('./menu.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        if item_id >= len(contents):
            return {'message': 'item_id does not exist'}

        return contents[item_id][price_index]


class Order(Resource):
    def get(self):
        loaded_contents = json.load(open('orders.json', 'r'))
        return loaded_contents

    def post(self):
        loaded_contents = json.load(open('orders.json', 'r'))
        new_order_id = max([int(key) for key in loaded_contents.keys()]) + 1 if len(loaded_contents) > 0 else 1

        loaded_contents[new_order_id] = {}
        json.dump(loaded_contents, open('orders.json', 'w'))

        return new_order_id


class OrderOperation(Resource):
    def get(self, order_id):
        order_id = str(order_id)
        loaded_contents = json.load(open('orders.json', 'r'))
        if order_id not in loaded_contents.keys():
            return {'message': 'order id {0} does not exist'.format(order_id)}

        return loaded_contents[order_id]

    def delete(self, order_id):
        order_id = str(order_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if str(order_id) not in loaded_contents.keys():
            return {'message': 'order id {0} does not exist'.format(order_id)}

        loaded_contents.pop(order_id)
        json.dump(loaded_contents, open('orders.json', 'w'))
        return {'message': 'order id {0} has been deleted'.format(order_id)}


class OrderItem(Resource):
    def post(self, order_id, item_id):
        order_id, item_id = str(order_id), str(item_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if str(order_id) not in loaded_contents.keys():
            return {'error message': 'the order id does not exist'}

        # added new item id as a key
        loaded_contents[order_id][item_id] = []
        json.dump(loaded_contents, open('orders.json', 'w'))

        return {"message": "updated order details"}

    def delete(self, order_id, item_id):
        order_id, item_id = str(order_id), str(item_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if str(order_id) not in loaded_contents.keys():
            return {'error message': 'the order id does not exist'}

        # item is deleted from orders
        del(loaded_contents[order_id][item_id])
        json.dump(loaded_contents, open('orders.json', 'w'))

        return {"message": "updated order details"}


class PizzaTopping(Resource):
    def post(self, order_id, pizza_item_id, topping_item_id):
        order_id, pizza_item_id, topping_item_id = str(order_id), str(pizza_item_id), str(topping_item_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if order_id not in loaded_contents:
            return {'error message': 'the order id does not exist'}

        if pizza_item_id not in loaded_contents[order_id]:
            return {'error message': 'the pizza item id not in order'}

        # forbid duplicated toppings to be added twice
        if pizza_item_id in loaded_contents[order_id] and topping_item_id not in loaded_contents[order_id][pizza_item_id]:
            loaded_contents[order_id][pizza_item_id].append(topping_item_id)

        json.dump(loaded_contents, open('orders.json', 'w'))
        return loaded_contents[order_id]

    def delete(self, order_id, pizza_item_id, topping_item_id): #     order_id, pizza_item_id, topping_item_id = str(order_id), str(pizza_item_id), str(topping_item_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if order_id not in loaded_contents:
            return {'error message': 'the order id does not exist'}

        if pizza_item_id not in loaded_contents[order_id]:
            return {'error message': 'the pizza item id not in order'}

        toppings = set(loaded_contents[order_id][pizza_item_id])

        if topping_item_id not in toppings:
            return {'message': 'topping is not used on Pizza'}

        toppings.remove(topping_item_id)
        loaded_contents[order_id][pizza_item_id] = list(toppings)
        json.dump(loaded_contents, open('orders.json', 'w'))

        return {"message": "topping id {} deleted from order".format(topping_item_id)}


class PickUp(Resource):
    def post(self, order_id):
        order_id = str(order_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if str(order_id) not in loaded_contents.keys():
            return {'error message': 'the order id does not exist'}

        # item is deleted from orders
        del(loaded_contents[order_id])
        json.dump(loaded_contents, open('orders.json', 'w'))

        return {"message": "order id {} is picked up".format(order_id)}


class Delivery(Resource):
    def post(self, order_id, method, address):
        order_id = str(order_id)
        loaded_contents = json.load(open('orders.json', 'r'))

        if str(order_id) not in loaded_contents.keys():
            return {'error message': 'the order id does not exist'}

        order_details_json = {
            "details": loaded_contents[order_id],
            "method": method,
            "address": address
        }

        del(loaded_contents[order_id])
        return order_details_json


api.add_resource(Menu, '/menu')
api.add_resource(ItemPrice, '/itemPrice/<int:item_id>')
api.add_resource(Order, '/order')
api.add_resource(OrderOperation, '/order/<int:order_id>')
api.add_resource(OrderItem, '/orderItem/<int:order_id>/<int:item_id>')
api.add_resource(PizzaTopping, '/pizzaTopping/<string:order_id>/<string:pizza_item_id>/<string:topping_item_id>')
api.add_resource(PickUp, '/pickup/<int:order_id>')
api.add_resource(Delivery, '/delivery/<string:order_id>/<string:method>/<string:address>')

if __name__ == "__main__":
    app.run(debug=True)
