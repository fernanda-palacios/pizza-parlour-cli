import click


@click.group()
def order():
    pass

    
@order.command()
def create_order():
    click.echo('create_order was called')

@order.command()
def see_order():
    click.echo('see_order was called')

@order.command()
def update_order():
    click.echo('update_order was called')