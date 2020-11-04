import click
import requests


@click.group()
def order():
    pass

    
@order.command()
def create_order():
    url_format = 'http://127.0.0.1:5000/order'
    response = requests.post(url_format)
    click.echo(response.text) 


@order.command()
@click.option('--order_id')
@click.option('--item_id')
def add_item_to_order(order_id, item_id):
    url_format = 'http://127.0.0.1:5000/orderItem'

    query_params = {
        'order_id': order_id,
        'item_id': item_id
    }

    response = requests.post(url_format, params=query_params)
    click.echo(response.text) 

@order.command()
@click.option('--order_id')
@click.option('--item_id')
def remove_item_from_order(order_id, item_id):
    url_format = 'http://127.0.0.1:5000/orderItem'
    response = requests.post(url_format)
    
    query_params = {
        'order_id': order_id,
        'item_id': item_id
    }

    response = requests.delete(url_format, params=query_params)
    click.echo(response.text) 



@order.command()
@click.option('--order_id')
@click.option('--pizza_item_id')
@click.option('--topping_item_id')
def add_topping_to_pizza(order_id, pizza_item_id, topping_item_id):
    url_format = 'http://127.0.0.1:5000/pizzaTopping'

    query_params = {
        'order_id': order_id,
        'pizza_item_id': pizza_item_id,
        'topping_item_id': topping_item_id
    }

    response = requests.post(url_format, params=query_params)
    click.echo(response.text) 



@order.command()
@click.option('--order_id')
@click.option('--pizza_item_id')
@click.option('--topping_item_id')
def remove_topping_from_pizza(order_id, pizza_item_id, topping_item_id):
    url_format = 'http://127.0.0.1:5000/pizzaTopping'

    query_params = {
        'order_id': order_id,
        'pizza_item_id': pizza_item_id,
        'topping_item_id': topping_item_id
    }

    response = requests.delete(url_format, params=query_params)
    click.echo(response.text) 


@order.command()
@click.option('--order_id')
def see_order(order_id):
    url_format = 'http://127.0.0.1:5000/order'
    
    query_params = {
        'order_id': order_id
    }

    response = requests.get(url_format, params=query_params)
    click.echo(response.text) 


@order.command()
@click.option('--order_id')
def cancel_order(order_id):
    url_format = 'http://127.0.0.1:5000/order'
    
    query_params = {
        'order_id': order_id
    }

    response = requests.delete(url_format, params=query_params)
    click.echo(response.text) 
    