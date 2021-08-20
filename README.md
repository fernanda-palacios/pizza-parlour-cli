# Pizza Parlour CLI App

### Local setup
- `pip install -r requirements.txt` install dependencies
- `python3 -m pip install --editable .` for CLI app to work with the entry point of `cli`

### Running app locally
- First, run the server: `python3 API.py`
- The CLI can then be used on a separate shell. CLI commands can be invoked as `cli {group} {command}` (examples section available below)

*Note: The commands are divided by groups (`menu`, `order`, `pickup-or-delivery`) and each group has its own available comands (e.g. `cli menu see-full-menu`)(full documentation below)

### Menu and item id's
The menu can be found / modified in [menu.csv](https://github.com/fernanda-palacios/pizza-parlour-cli/blob/main/menu.csv)\
<img src="various_readme_pictures/menu.png" alt="menu" height="350" width="250"/>


### Example usage of CLI/ documentation

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
