from flask import Flask

app = Flask("Assignment 2")

@app.route('/pizza')
def welcome_pizza():
    return 'Welcome to Pizza Planet!'

@app.route('/menu')
def get_menu():
    return 'this would be the menu'

if __name__ == "__main__":
    app.run()
