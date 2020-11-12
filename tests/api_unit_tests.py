from API import app
import json


# Menu
def test_get_menu():
    response = app.test_client().get('/menu')
    assert response.status_code == 200


# ItemPrice
def test_get_item_price():
    response = app.test_client().get('/itemPrice/1')
    assert response.status_code == 200


def test_get_non_existing_item_price():
    response = app.test_client().get('/itemPrice/100')
    assert response.status_code == 200


# Order
def test_get_order():
    response = app.test_client().get('/order')
    assert response.status_code == 200


def test_post_order():
    response = app.test_client().post('/order')
    assert response.status_code == 200


# OrderOperation
def test_get_non_existing_order():
    targeted_order_id = 100
    response = app.test_client().get('/order/{}'.format(targeted_order_id))
    assert response.status_code == 200


def test_get_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "1"
    loaded_contents[targeted_order_id] = {}
    json.dump(loaded_contents, open('orders.json', 'w'))
    response = app.test_client().get('/order/{}'.format(targeted_order_id))
    assert response.status_code == 200


def test_delete_non_existing_order():
    targeted_order_id = 100
    response = app.test_client().delete('/order/{}'.format(targeted_order_id))
    assert response.status_code == 200


def test_delete_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "10000000"
    loaded_contents[targeted_order_id] = {}
    json.dump(loaded_contents, open('orders.json', 'w'))
    response = app.test_client().delete('/order/{}'.format(targeted_order_id))
    assert response.status_code == 200


# OrderItem
def test_post_item_to_non_existing_order():
    targeted_order_id = 1000000
    targeted_item_id = 1
    response = app.test_client().post('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


def test_post_item_to_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "1"
    loaded_contents[targeted_order_id] = {}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_item_id = 1
    response = app.test_client().post('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


def test_delete_item_from_non_existing_order():
    targeted_order_id = 100
    targeted_item_id = 1
    response = app.test_client().delete('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


def test_delete_item_from_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "1"
    loaded_contents[targeted_order_id] = {1:[]}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_item_id = 1
    response = app.test_client().delete('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200

# Pizza
def test_post_topping_to_non_existing_order():
    targeted_order_id = 10000
    targeted_pizza_item_id = 1
    targeted_topping_item_id = 4
    response = app.test_client().post('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


def test_post_topping_to_non_existing_pizza():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "1"
    loaded_contents[targeted_order_id] = {1:[]}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_pizza_item_id = 2
    targeted_topping_item_id = 4
    response = app.test_client().post('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


def test_post_topping_to_existing_pizza():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "1"
    loaded_contents[targeted_order_id] = {1:[]}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_pizza_item_id = 1
    targeted_topping_item_id = 4
    response = app.test_client().post('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


def test_delete_topping_from_non_existing_order():
    targeted_order_id = 100
    targeted_item_id = 1
    response = app.test_client().delete('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


def test_delete_topping_from_non_existing_pizza():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = 1
    targeted_pizza_item_id = 2
    targeted_topping_item_id = 4

    loaded_contents[targeted_order_id] = {1: []}

    json.dump(loaded_contents, open('orders.json', 'w'))
    response = app.test_client().delete('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


def test_delete_not_used_topping():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = 1
    loaded_contents[targeted_order_id] = {1: ["4"]}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_pizza_item_id = 1
    targeted_topping_item_id = 3
    response = app.test_client().delete('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


def test_delete_topping_from_existing_pizza():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = 1
    loaded_contents[targeted_order_id] = {1: ["4"]}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    targeted_pizza_item_id = 1
    targeted_topping_item_id = 4
    response = app.test_client().delete('/pizzaTopping/{}/{}/{}'.format(
        targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
    ))
    assert response.status_code == 200


# Pickup
def test_pick_up_non_existing_order():
    targeted_order_id = 10000
    response = app.test_client().post('/pickup/{}'.format(targeted_order_id))
    assert response.status_code == 200


def test_pick_up_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = 1
    loaded_contents[targeted_order_id] = {1: []}
    json.dump(loaded_contents, open('orders.json', 'w'))
    targeted_order_id = 1
    response = app.test_client().post('/pickup/{}'.format(targeted_order_id))
    assert response.status_code == 200


# Delivery
def test_delivery_non_existing_order_id():
    targeted_order_id = 100000
    targeted_method = "uber-eats"
    targeted_address = "Toronto"
    response = app.test_client().post('/delivery/{}/{}/{}'.format(
        targeted_order_id, targeted_method, targeted_address))
    assert response.status_code == 200


def test_delivery_existing_order_id():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = 1
    loaded_contents[targeted_order_id] = {1: ["4"]}
    json.dump(loaded_contents, open('orders.json', 'w'))

    targeted_method = "uber-eats"
    targeted_address = "Toronto"
    response = app.test_client().post('/delivery/{}/{}/{}'.format(
        targeted_order_id, targeted_method, targeted_address))
    assert response.status_code == 200
