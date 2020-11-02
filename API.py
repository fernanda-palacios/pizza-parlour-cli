from flask import Flask
from flask_restful import Api, Resource

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


class Order(Resource):
    def post(self, order_number, pizza_order_details, drink):
        """
        :param order_number: example 245
        :param pizza_order_details: example {"Size": 'large', "Type": "epperoni", "Toppings": ["olives", "tomatoes"]}
        # todo pizza might be multiples?
        :param drink: ["Coke", "Diet Coke"]
        """
        # Todo order_number and total order prices will be stored in file?
        pass

    def update(self, order_number, pizza_order_details, drink):
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

if __name__ == "__main__":
    app.run()
