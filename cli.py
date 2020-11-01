import click
import requests
from cli_commands.menu import menu
from cli_commands.order import order


@click.group()
def cli():
    pass

# @cli.command()
# def menu():
#     click.echo('menu called')

# @cli.command()
# def create_order():
#     click.echo('create_order')

# @cli.command()
# def see_order():
#     click.echo('see_order')

# @cli.command()
# def update_order():
#     click.echo('update_order')

@cli.command()
def select_pickup_or_delivery_method():
    click.echo('select_pickup_or_delivery_method')

# additional more complex interaction examples

@cli.command()
@click.argument('arg')
def with_api_request(arg):
    click.echo('with_api_request')
    click.echo(arg)
    url_format = 'http://127.0.0.1:5000/pizza'
    response = requests.get(url_format)
    click.echo(response.text) 


@cli.command()
@click.option('--n', default=1, show_default=True)
# usage: cli dots --n=3
def dots(n):
    click.echo('.' * n)


@cli.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
              
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

def main():
    value = click.prompt('Select a command to run', type=click.Choice(list(cli.commands.keys())))
    cli.commands[value]()


cli.add_command(menu)
cli.add_command(order)


if __name__ == "__main__":
    main()
