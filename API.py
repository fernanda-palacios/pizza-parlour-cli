from flask import Flask
from flask_restful import Api, Resource

import csv

app = Flask(__name__)
api = Api(app)


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


api.add_resource(Menu, '/menu')

if __name__ == "__main__":
    app.run()
