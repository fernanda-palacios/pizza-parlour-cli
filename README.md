# A2


## 1. Instructions for using app

### Setup
- `pip install -r requirements.txt` install dependencies
- `python3 -m pip install --editable .` for cli app to work with the entry point of 'cli'


### Running the cli app
The commands are divided by groups (categories) and each group has its own available comands
Any command can be invoked as `cli {group} {command}` (examples section below)

**CLI Groups:**

![alt text](cli_instructions_pictures/groups.png)


**Comands for each group**
![alt text](cli_instructions_pictures/menu_commands.png)

![alt text](cli_instructions_pictures/order_commands.png)

![alt text](cli_instructions_pictures/pickup-or-delivery_commands.png)



Note: a cli method might be implemented as `see_full_menu` but it needs to be called as `see-full-menu` (with dashes not underscores) 


### Running the server
Run the main Flask module by running `python3 API.py`

### Running tests
- Run API unit tests with coverage by running `pytest --cov-report term --cov=. tests/api_unit_tests.py`

- Run our CLI tests with coverage by running `pytest --cov-report term --cov=. tests/cli_tests.py`


## 2. Pair Programming

## 3. Program Design

## 4. Tools Used (code craftsmanship)


