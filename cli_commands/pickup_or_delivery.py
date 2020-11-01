import click


@click.group()
def pickup_or_delivery():
    pass

    
@pickup_or_delivery.command()
def select_pickup_or_delivery_method():
    click.echo('select_pickup_or_delivery_method was called')
