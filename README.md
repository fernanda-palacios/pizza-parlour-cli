# A2


## Instructions for using app

### Setup

1. Installing dependencies 
- `pip install -r requirements.txt`
<!-- - `pip install flask`
- `pip install pytest`
- `pip install pytest-cov`
- `pip install flask_restful` -->
- `python3 -m pip install --editable .` for cli app to work with the entry point of 'cli'


### Running the cli app
`python3 cli.py` or `cli {command}` 

`cli --help` see documentation for cli (available commands and arguments)

`cli {command} --help` see documentation for that command (available subcommands and arguments)

    - for commands nested inside groups, invoke them as  `cli {command} {subcommand}` eg `cli menu see-full-menu`


Note: a cli method might be implemented as `see_full_menu` but it needs to be called as `see-full-menu` (with dashes not underscore) from the cli (it might be a click thing)


### Running the server
Run the main Flask module by running `python3 PizzaParlour.py`

### Running unit tests
- Run API unit tests `pytest tests/api_unit_tests.py`

- Run API unit tests with coverage by running `pytest --cov-report term --cov=. tests/api_unit_tests.py`

- Run CLI (poc) unit tests with coverage by running `pytest --cov-report term --cov=. tests/test_sync.py  `

 - Run our CLI (poc) unit tests with coverage by running `pytest --cov-report term --cov=. tests/cli_tests.py`


## Pair Programming

## Program Design

## Tools Used (code craftmanship)


