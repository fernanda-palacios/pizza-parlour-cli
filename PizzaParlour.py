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


@app.route('/order', methods=['POST', 'GET', 'DELETE'])
def create_order():
    if request.method == 'POST':
        return 'create order response POST'
    elif request.method == 'GET': 
        order_id = request.args['order_id']    
        return 'create order response GET, id: ' + order_id
    else:
        order_id = request.args['order_id']    
        return 'create order response DELETE, id' + order_id

        


@app.route('/orderItem', methods=['POST', 'DELETE'])
def handle_order_item():
    if request.method == 'POST':
        order_id = request.args['order_id']    
        item_id = request.args['item_id']    

        return 'handle_order_item response POST ' + order_id + ', ' + item_id

    else:
        order_id = request.args['order_id']    
        item_id = request.args['item_id']    

        return 'handle_order_item response DELETE' + order_id + ', ' + item_id



@app.route('/pizzaTopping', methods=['POST', 'DELETE'])
def handle_pizza_topping():
    if request.method == 'POST':
        order_id = request.args['order_id']    
        pizza_item_id = request.args['pizza_item_id'] 
        topping_item_id = request.args['topping_item_id']    

        return 'handle_pizza_toppinging_to_pizza response POST ' + order_id + ', ' + pizza_item_id + ', ' + topping_item_id
    else:
        order_id = request.args['order_id']    
        pizza_item_id = request.args['pizza_item_id'] 
        topping_item_id = request.args['topping_item_id']    

        return 'handle_pizza_toppingg response DELETE' + order_id + ', ' + pizza_item_id + ', ' + topping_item_id

  




if __name__ == "__main__":
    app.run()
