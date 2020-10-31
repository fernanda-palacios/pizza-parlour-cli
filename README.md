# a2-starter

### CLI commands with flask
`flask hello`  - input name and return greetings.


### CLI command app
`python3 cli.py` or `cli {command}` 

`cli --help` see documentation for cli (available commands and arguments)


### Setup the environment
`pip3 install flask pytest`
`python3 -m pip install --editable .` for cli app to work with the entry point of 'cli'

### Running the server
Run the main Flask module by running `python3 PizzaParlour.py`

Then open `http://127.0.0.1:5000/pizza` to see the welcome screen

### Running unit tests
- Run unit tests `pytest tests/unit_tests.py`

- Run unit tests with coverage by running `pytest --cov-report term --cov=. tests/unit_tests.py`


### Installing dependencies 
- `pip install flask`
- `pip install pytest`
- `pip install pytest-cov`
