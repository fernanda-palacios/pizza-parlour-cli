import click


@click.group()
def menu():
    pass


@menu.command()
def see_full_menu():
    click.echo('see full menu was called')


@menu.command()
def item_price():
    click.echo('item price was called')
    