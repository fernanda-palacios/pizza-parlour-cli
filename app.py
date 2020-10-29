'''
useful tutorials belows
- About click
https://click.palletsprojects.com/en/7.x/

- flask + click official document
https://flask.palletsprojects.com/en/1.1.x/cli/

- flask + click youtube tutorial
https://www.youtube.com/watch?v=wyG3BiL-E5c&t=20s&ab_channel=PrettyPrinted
'''

from flask import Flask
import click

app = Flask(__name__)

@click.command()
@click.option('--name', prompt='Hi, what is your name?', help='The person to greet.')

def hello(name):
    """Simple program that greets NAME"""
    click.echo('User enters %s' % name)
    click.echo('Program logs Hi %s' % name)

app.cli.add_command(hello)