import click


@click.group()
def cloudflare():
    pass


@cloudflare.command()
def zone():
    click.echo('This is the zone subcommand of the cloudflare command')
    