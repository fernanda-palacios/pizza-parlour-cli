import click

@click.group()
def cli():
    pass

@cli.command()
def create():
    click.echo('create called')
    # os.system('curl http://127.0.0.1:5000/create')

@cli.command()
def conn():
    click.echo('conn called')
    # os.system('curl http://127.0.0.1:5000/')

@cli.command()
def new():
    click.echo('new called')
    # os.system('curl http://127.0.0.1:5000/')

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

if __name__ == "__main__":
    main()
