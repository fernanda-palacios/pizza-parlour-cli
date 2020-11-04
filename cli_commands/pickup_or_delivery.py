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
    click.echo(response.text) 



    
# @pickup_or_delivery.command()
# def select_pickup_or_delivery_method():
#     click.echo('select_pickup_or_delivery_method was called')
