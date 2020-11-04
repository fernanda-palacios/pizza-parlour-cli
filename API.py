from flask import Flask
from flask_restful import Api, Resource

import csv

app = Flask(__name__)
api = Api(app)


class Drinks(Resource):
    def get(self):
        drinks_types = ["Coke", "Diet Coke", "Coke Zero", "Pepsi", "Diet Pepsi", "Dr.Pepper"]
        return {"items": drinks_types}


class Pizza(Resource):
    def get(self):
        pizza_types = ["epperoni", "margherita", "vegetarian", "Neapolitan"]
        return {"items": pizza_types}


class Toppings(Resource):
    def get(self):
        toppings_types = ["olives", "tomatoes", "mushrooms", "jalapenos", "chicken", "beef", "pepperoni"]
        return {"items": toppings_types}


class Prices(Resource):
    def get(self):
        # todo: read file contents where the prices of each items are specified and return the json for those data
        pass


class Item(Resource):
    # Todo item idを受け取る方法を調べる。
    def get(self, item_id):
        price_index = 4
        with open('./menu.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        return contents[item_id + 1][price_index]


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
        with open('./orders.csv') as file:
            reader = csv.reader(file)
            contents = [row for row in reader]

        return {'contents': contents}

    def post(self, order_id, pizza_order_details, drink_order_details):
        """
        # :param order_id: example 245
        # :param pizza_order_details: example {"Size": 'large', "Type": "epperoni", "Toppings": ["olives", "tomatoes"]}
        # # {0: {Size: hoge, Type: hoge} Toppings = {0: [hoge, hoge]}
        # # todo pizza might be multiples?
        # :param drinks: ["Coke", "Diet Coke"]
        :param pizzas: {0: 1, 1: 2}} - with pizza id
        :param drinks: [15, 24] - with pizza id
        :param toppings: {0: [13, 14], 1: [23, 34]}
        """
        # Todo order_number and total order prices will be stored in file?
    #     # item id + topping id + drinks id = price
    #     Todo 基本的にIDを投げてもらう。Size や typeに応じてIDを検索できるmethodを返す。

    def update(self, order_number, pizzas, drinks, toppings):
        pass

    def cancel(self, order_number):
        pass

    def fetch(self, order_number):
        # Todo have to know how delivery and pickup works
        pass


api.add_resource(Drinks, '/drinks')
api.add_resource(Pizza, '/pizza')
api.add_resource(Toppings, '/toppings')
api.add_resource(Prices, '/prices')
api.add_resource(Order, '/order')
api.add_resource(Menu, '/menu')

if __name__ == "__main__":
    app.run()
