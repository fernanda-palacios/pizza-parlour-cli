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


@app.route('/addToOrder', methods=['POST'])
def add_item_to_order():
    order_id = request.args['order_id']    
    item_id = request.args['item_id']    

    return 'add_item_to_order response ' + order_id + ', ' + item_id


@app.route('/removeFromOrder', methods=['POST'])
def remove_item_from_order():

    order_id = request.args['order_id']    
    item_id = request.args['item_id']    

    return 'remove item from order response' + order_id + ', ' + item_id
        


if __name__ == "__main__":
    app.run()
