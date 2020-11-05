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
    def post(self):
        loaded_contents = json.load(open('orders.json', 'r'))
        new_order_id = max([int(key) for key in loaded_contents.keys()]) + 1

        loaded_contents[new_order_id] = {}
        json.dump(loaded_contents, open('orders.json', 'w'))

        return new_order_id


api.add_resource(Order, '/order')
api.add_resource(Menu, '/menu')
api.add_resource(ItemPrice, '/itemPrice/<int:item_id>')


if __name__ == "__main__":
    app.run()
