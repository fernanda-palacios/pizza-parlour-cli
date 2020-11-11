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


# OrderDelete
def test_delete_non_existing_order():
    targeted_order_id = 100
    response = app.test_client().delete('/order/{}'.format(targeted_order_id))
    assert response.json == {'message': 'order id {0} does not exist'.format(targeted_order_id)}


def test_delete_existing_order():
    loaded_contents = json.load(open('orders.json', 'r'))
    targeted_order_id = "10000000"
    loaded_contents[targeted_order_id] = {}
    json.dump(loaded_contents, open('orders.json', 'w'))
    response = app.test_client().delete('/order/{}'.format(targeted_order_id))
    assert response.status_code == 200


# OrderItem
def test_post_item_to_non_existing_order():
    targeted_order_id = 100
    targeted_item_id = 1
    response = app.test_client().post('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


# Todo: can be improved
def test_post_item_to_existing_order():
    targeted_order_id = 1
    targeted_item_id = 1
    response = app.test_client().post('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


def test_delete_item_from_non_existing_order():
    targeted_order_id = 100
    targeted_item_id = 1
    response = app.test_client().delete('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
    assert response.status_code == 200


# def test_delete_item_from_existing_order():
#     targeted_order_id = 100
#     targeted_item_id = 1
#     response = app.test_client().delete('/orderItem/{}/{}'.format(targeted_order_id, targeted_item_id))
#     assert response.status_code == 200

# def test_pick_up():
#     targeted_order_id = 100
#     response = app.test_client().post('/pickup/{}'.format(targeted_order_id))
#     assert response.status_code == 200
#
#
# def test_post_pizza_topping():
#     targeted_order_id = 100
#     targeted_pizza_item_id = 1
#     targeted_topping_item_id = 4
#     response = app.test_client().post('/pizzaTopping/{}/{}/{}'.format(
#         targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
#     ))
#     assert response.status_code == 200
#
#
# def test_delete_pizza_topping():
#     targeted_order_id = 100
#     targeted_pizza_item_id = 1
#     targeted_topping_item_id = 4
#     response = app.test_client().delete('/pizzaTopping/{}/{}/{}'.format(
#         targeted_order_id, targeted_pizza_item_id, targeted_topping_item_id
#     ))
#     assert response.status_code == 200
#
