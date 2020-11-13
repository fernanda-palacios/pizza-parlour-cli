import click
import requests


@click.group()
def pickup_or_delivery():
    pass


@pickup_or_delivery.command()
@click.option('--order_id')
def select_pickup(order_id):
    url_format = 'http://127.0.0.1:5000/pickup'
    response = requests.post(url_format + '/{}'.format(order_id))
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

    response = requests.post(
        url_format + '/{}/{}/{}'.format(order_id, method, address, order_details_format))
    click.echo('Delivery has been selected')
    click.echo(response.text)
