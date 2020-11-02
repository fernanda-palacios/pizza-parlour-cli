from flask import Flask
from flask import jsonify
from flask import request


app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

# for sending back json responses: https://flask.palletsprojects.com/en/1.1.x/api/#module-flask.json
@app.route('/menu')
def get_menu():
    return jsonify(coke=10,
                   water=20)

@app.route('/itemPrice')
def get_item_price():
    item_id = request.args['item_id']    
    return "will send back price for item with id:" + item_id


@app.route('/order', methods=['POST'])
def create_order():
    return 'create order response'


@app.route('/addToOrder')
def add_item_to_order():
    return 'add_item_to_order response'


@app.route('/removeFromOrder')
def remove_item_from_order():
    return 'remove item from order response'
    


if __name__ == "__main__":
    app.run()
