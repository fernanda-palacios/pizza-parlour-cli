import click
import requests


@click.group()
def menu():
    pass


@menu.command()
def see_full_menu():
    url_format = 'http://127.0.0.1:5000/menu'
    response = requests.get(url_format)
    click.echo('Menu:')
    click.echo(response.text)


@menu.command()
@click.option('--item_id')
def item_price(item_id):
    url_format = 'http://127.0.0.1:5000/itemPrice'
    response = requests.get(url_format + '/' + item_id)
    click.echo('Price:')
    click.echo(response.text)
