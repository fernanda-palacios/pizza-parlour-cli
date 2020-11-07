from flask import Flask
from flask_restful import Api, Resource


import csv, json

app = Flask(__name__)
api = Api(app)


class ItemPrice(Resource):
    def get(self, item_id):
        price_index = 4
        with open('./menu.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        if item_id >= len(contents):
            return {'message': 'item_id does not exist'}

        return contents[item_id][price_index]


class Menu(Resource):
    def get(self):
        with open('./menu.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        # return {'menu': contents}
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


class Order(Resource):
    def get(self):
        loaded_contents = json.load(open('orders.json', 'r'))
        return {'orders': loaded_contents}

    def post(self):
        loaded_contents = json.load(open('orders.json', 'r'))

        if len(loaded_contents) == 0:
            new_order_id = 1
        else:
            new_order_id = max([int(key) for key in loaded_contents.keys()]) + 1

        loaded_contents[new_order_id] = {}
        json.dump(loaded_contents, open('orders.json', 'w'))

        return new_order_id

    def delete(self, order_id):
        loaded_contents = json.load(open('orders.json', 'r'))
        loaded_contents.pop(str(order_id))
        json.dump(loaded_contents, open('orders.json', 'w'))


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
        loaded_contents[order_id][pizza_item_id].append(topping_item_id)

        # jsonify的なのいるかも
        return loaded_contents

        return {"updated order details": {loaded_contents[order_id]}}

    def delete(self, order_id, pizza_item_id, topping_item_id):
        loaded_contents = json.load(open('orders.json', 'r'))

        if order_id not in loaded_contents:
            return {'error message': 'the order id does not exist'}

        if pizza_item_id not in loaded_contents[order_id]:
            return {'error message': 'the pizza item id not in order'}

        # toppingをsetにした方がいいかもしれない？ 絶対
        loaded_contents[order_id][pizza_item_id].remove(topping_item_id)

        return {"updated order details": {loaded_contents[order_id]}}


class PickUp(Resource):
    def post(self, order_id):
#         todo do same thing as cancel order


class Delivery(Resource):
    def post(self, order_id, method, address):
#         todo


api.add_resource(PickUp, '/pickup/<int:order_id>')
api.add_resource(PizzaTopping, '/pizzaTopping/<int:order_id>/<int:pizza_item_id>/<int:topping_item_id>')
api.add_resource(OrderItem, '/orderItem/<int:order_id>/<int:item_id>')
api.add_resource(Order, '/order')
api.add_resource(Menu, '/menu')
api.add_resource(ItemPrice, '/itemPrice/<int:item_id>')

if __name__ == "__main__":
    app.run()
