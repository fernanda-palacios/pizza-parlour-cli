import click
import requests

@click.group()
def menu():
    pass


@menu.command()
def see_full_menu():
    click.echo('see full menu was called')
    url_format = 'http://127.0.0.1:5000/menu'
    response = requests.get(url_format)
    click.echo(response.text) 


@menu.command()
def item_price():
    click.echo('item price was called')
    