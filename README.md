# A2


## 1. Instructions for using app

### Setup
- `pip install -r requirements.txt` install dependencies
- `python3 -m pip install --editable .` for CLI app to work with the entry point of `cli`


### Running the pizza parlour application

- First, run the server: `python3 API.py`
- The CLI can then be used on a separate shell. CLI commands can be invoked as `cli {group} {command}` (examples section available below)

*Note: The commands are divided by groups (`menu`, `order`, `pickup-or-delivery`) and each group has its own available comands (e.g. `cli menu see-full-menu`)(full documentation below)


### Menu and item id's

The menu is organized based on item id's (first column), required to use the application.
![alt text](various_readme_pictures/menu.png)



### Example usage of CLI/ documentation


Features based on category/groups:

- Menu
  - See  menu: 
    -  `cli menu see-full-menu`
  - Get price of an item:
    - `cli menu item-price --item_id={item_id}`

- Order: 
  - Create a new order (**returns an order id - needed to add items to order**) 
    - `cli order create-order`

  - Add item to order (only pizza or drinks): 
    - `cli order add-item-to-order --order_id={order_id} --item_id={item_id}`

  - Remove item from order  (only pizza or drinks): : 
     - `cli order remove-item-from-order --order_id={order_id} --item_id={item_id}`

  - Add topping to pizza: 
    - `cli order add-topping-to-pizza --order_id={order_id} --pizza_item_id={pizza_item_id} --topping_item_id={topping_item_id}`

  - Remove topping from pizza: 
    - `cli order remove-topping-from-pizza --order_id={order_id} --pizza_item_id={pizza_item_id} --topping_item_id={topping_item_id}`

  - See order (order details): 
    - `cli order see-order --order_id={order_id}`

  - Cancel order: 
    - `cli order cancel-order --order_id={order_id}`

- Ask for pickup/delivery:
    - Pickup:
      - `cli  pickup-or-delivery select-pickup --order_id={order_id}`

    - Delivery
      -  `cli  pickup-or-delivery select-delivery-method --order_id={order_id} --method={one of: ‘ubereats’, ‘in-house’, ‘foodora’} --address={address}`


*Note: ensure the CLI is used with valid cases (cancel an existing order, add pizza then topping, remove existing item, modify order before selecting pickup/delivery, etc)


*Note: a CLI method might be implemented as `see_full_menu` but it needs to be called as `see-full-menu` (with dashes not underscores) 



#### Dynamically changing prices / customizing items:
If a client wishes to customize the prices used while running the application or to include a new pizza / item, they can do so by modifying the content from `menu.csv`: https://github.com/csc301-fall-2020/assignment-2-33-shiseru-fernandapalacios/blob/main/menu.csv



## 2. Running tests and coverage

- Run API unit tests with coverage for **API files** by running `pytest --cov-report term --cov=. tests/api_unit_tests.py`

- Run our CLI tests with coverage for **CLI files** by running `pytest --cov-report term --cov=. tests/cli_tests.py`


## 3. Pair Programming

We firstly used Visual Studio Code live share plugin to conduct the pair programming. Then, everyday we held 30 mins conversation using zoom to discuss the assignment.

While doing pair programming, we separated this process into three different phases of development.

1. Clarify the client requirements and design the command line interface accordingly
- To set the correct backend API, having a clear idea of what the application would do from the client’s perspective was mandatory. In this part, Fernanda was mainly responsible for coming up with the command line interface design and architecture, and she discussed with Shisei the details for the required commands. 

2. Set up the backend API mock up
- When the front-end design and architecture was done, we started discussing backend API design. In this part, Shisei was mainly responsible for developing the design. While we were discussing the backend API designs, we chose to use REST API with Flask-RESTful plugin as it constructs each API based on the concept of modularity and single responsibility by defining each API into separate classes. 

3. Actual coding. 
For the command line interface, Fernanda played the driver's role while Shisei was taking Navigator's role. Shisei was specifying what to code based on the mock command line interface discussed during phase 1. When the driver feels that there's lack of clarity, the driver and the navigator discuss and clarify. Also as Shisei played the role of navigator, he conducted syntax error checking which Fernanda coded.

For backend API coding, we switched role vice versa and conducted pair programming to write actual codes.

Overall, we deeply focused on communication while pair programming. We usually try to share our thoughts to keep ourselves on the same pages. That made it easier to discover the pitfalls while coding.


## 4. Program Design

We focused on applying the following coding principles:

1. DRY (Don't repeat yourself) - for frontend and backend, if the same codes appear in different functions, we write it out as a separate function. For instance, in the file test/api_unit_tests.py, as we had to generate fake data over and over again in different test cases, we extracted the generated data part as a different function "load_empty_data" so that we avoid having the same codes in different test functions.

2. SLAP (Single level of abstraction) - especially for server API coding, we attempt to keep classes in the same abstraction level. For the APIs, we use the Flask-RESTful extension so that we can keep the API's in the same abstraction such as 'Delivery', 'Pickup', and 'Order'.  Similarly, for the command line interface, we applied this principle by grouping the commands and their modules into categories (menu, order, pickup or delivery).

3. Naming Convention - We follow the naming convention specified in the book "The Art of Readable Code" to name variables clearly for ease of interpretation. We especially focused on "avoid generic names like tmp", "prefer concrete names over abstract names", and "attaching extra information to a name" principles specified in the book. For instance, to name the test function for ‘get_order’ in the API, we avoided naming the test function to be 'test_order'. And we named the function to be 'test_get_existing_order' so that it clearly tells other team mate's that we are testing the GET request for order for the case that the order actually exists. The good naming convention fosters other team members to understand and extend the code more effectively.

## 5. Tools Used (code craftsmanship)

In order to have a good programming and formatting style in our code, we used the following tools to help us:
- IDE (Visual Studio Code) and its `format document` command in order to format code during local development. In order to use this command, we installed an extension on Visual Studio Code for formatting python based on the python's standard PEP 8 style guide.
- Linter github hook (autopep8 - which automatically formats Python code to conform to the PEP 8 style guide) (set up can be found here: https://github.com/csc301-fall-2020/assignment-2-33-shiseru-fernandapalacios/blob/main/.github/workflows/lint.yml


