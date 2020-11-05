import click
import requests

@click.group()
def menu():
    pass


@menu.command()
def see_full_menu():
    url_format = 'http://127.0.0.1:5000/menu'
    response = requests.get(url_format)
    click.echo('menu:')
    click.echo(response.text) 


@menu.command()
@click.option('--item_id')
def item_price(item_id):
    url_format = 'http://127.0.0.1:5000/itemPrice'

    query_params = {
        'item_id': item_id
    }

    response = requests.get(url_format, params=query_params)
    click.echo('price:')
    click.echo(response.text) 
    
