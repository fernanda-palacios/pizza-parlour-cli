# a2-starter

### CLI commands with flask
`flask hello`  - input name and return greetings.


### CLI commands without flask
`python3 cli.py --count=3`  - input name and return hello count times.


### Setup the environment
`pip3 install flask pytest`

### Running the app
Run the main Flask module by running `python3 PizzaParlour.py`

Then open `http://127.0.0.1:5000/pizza` to see the welcome screen

### Running unit tests
- Run unit tests `pytest tests/unit_tests.py`

- Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`


### Installing dependencies 
- `pip install flask`
- `pip install pytest`
- `pip install pytest-cov`
