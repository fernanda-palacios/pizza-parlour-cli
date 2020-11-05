import click
import requests
from cli_commands.menu import menu
from cli_commands.order import order
from cli_commands.pickup_or_delivery import pickup_or_delivery


@click.group()
def cli():
    pass

def main():
    value = click.prompt('Select a command to run', type=click.Choice(list(cli.commands.keys())))
    cli.commands[value]()


cli.add_command(menu)
cli.add_command(order)
cli.add_command(pickup_or_delivery)


if __name__ == "__main__":
    main()
