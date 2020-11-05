import click
import requests

@click.group()
def pickup_or_delivery():
    pass

    
@pickup_or_delivery.command()
@click.option('--order_id')
def select_pickup(order_id):
    url_format = 'http://127.0.0.1:5000/pickup'

    query_params = {
        'order_id': order_id
    }

    response = requests.post(url_format, params=query_params)
    click.echo('Pickup has been selected')
    click.echo(response.text) 



    
@pickup_or_delivery.command()
@click.option('--order_id')
@click.option('--method')
@click.option('--address')
def select_delivery_method(order_id, method, address):
    url_format = 'http://127.0.0.1:5000/delivery'

    if method == 'in-house' or method == 'ubereats':
        order_details_format = 'json'
    elif method == 'foodora': 
        order_details_format = 'csv'
  
    query_params = {
        'order_id': order_id,
        'method': method,
        'address': address,
        'order_details_format': order_details_format
    }

    response = requests.post(url_format, params=query_params)
    click.echo('Delivery has been selected')
    click.echo(response.text) 
