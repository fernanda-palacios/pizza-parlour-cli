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
    click.echo('add_item_to_order was called')

@order.command()
def remove_item_from_order():
    click.echo('remove_item_from_order was called')

@order.command()
def see_order():
    click.echo('see_order was called')

@order.command()
def update_order():
    click.echo('update_order was called')