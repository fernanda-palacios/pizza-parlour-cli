import click


@click.group()
def order():
    pass

    
@order.command()
def create_order():
    click.echo('create_order was called')

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