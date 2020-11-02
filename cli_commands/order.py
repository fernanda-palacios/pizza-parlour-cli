import click
import requests


@click.group()
def order():
    pass

    
@order.command()
def create_order():
    url_format = 'http://127.0.0.1:5000/order'
    response = requests.post(url_format)
    # TODO: parse json when echoing it
    click.echo(response.text) 


@order.command()
def add_item_to_order():
    url_format = 'http://127.0.0.1:5000/addToOrder'
    response = requests.post(url_format)
    # TODO: parse json when echoing it
    click.echo(response.text) 

@order.command()
def remove_item_from_order():
    url_format = 'http://127.0.0.1:5000/removeFromOrder'
    response = requests.post(url_format)
    # TODO: parse json when echoing it
    click.echo(response.text) 

@order.command()
def see_order():
    click.echo('see_order was called')
