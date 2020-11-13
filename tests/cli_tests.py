from click.testing import CliRunner
from cli import cli


def test_see_full_menu():
    runner = CliRunner()
    result = runner.invoke(cli, ['menu', 'see-full-menu'])
    assert result.exit_code == 0
    assert 'Menu:' in result.output


def test_item_price():
    runner = CliRunner()
    result = runner.invoke(cli, ['menu', 'item-price', '--item_id', '1'])
    assert result.exit_code == 0
    assert 'Price:' in result.output


def test_create_order():
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'create-order'])
    assert result.exit_code == 0
    assert 'Order has been created. Order Id:' in result.output


def test_add_item_to_order():
    runner = CliRunner()
    result = runner.invoke(
        cli, ['order', 'add-item-to-order', '--order_id', '1', '--item_id', '2'])
    assert result.exit_code == 0
    assert 'Added item to order' in result.output


def test_remove_item_from_order():
    runner = CliRunner()
    result = runner.invoke(
        cli, ['order', 'remove-item-from-order', '--order_id', '1', '--item_id', '2'])
    assert result.exit_code == 0
    assert 'Removed item from order' in result.output


def test_add_topping_to_pizza():
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['order',
                            'add-topping-to-pizza',
                            '--order_id',
                            '1',
                            '--pizza_item_id',
                            '2',
                            '--topping_item_id',
                            '3'])
    assert result.exit_code == 0
    assert 'Added topping to pizza' in result.output


def test_remove_topping_from_pizza():
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['order',
                            'remove-topping-from-pizza',
                            '--order_id',
                            '1',
                            '--pizza_item_id',
                            '2',
                            '--topping_item_id',
                            '3'])
    assert result.exit_code == 0
    assert 'Removed topping from pizza' in result.output


def test_see_order():
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'see-order', '--order_id', '1'])
    assert result.exit_code == 0
    assert 'Order details:' in result.output


def test_cancel_order():
    runner = CliRunner()
    result = runner.invoke(cli, ['order', 'cancel-order', '--order_id', '1'])
    assert result.exit_code == 0
    assert 'Order cancelled' in result.output


def test_select_pickup():
    runner = CliRunner()
    result = runner.invoke(
        cli, ['pickup-or-delivery', 'select-pickup', '--order_id', '1'])
    assert result.exit_code == 0
    assert 'Pickup has been selected' in result.output


def test_select_delivery_method_ubereats():
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['pickup-or-delivery',
                            'select-delivery-method',
                            '--order_id',
                            '1',
                            '--method',
                            'ubereats',
                            '--address',
                            '60 college st'])
    assert result.exit_code == 0
    assert 'Delivery has been selected' in result.output


def test_select_delivery_method_foodora():
    runner = CliRunner()
    result = runner.invoke(cli,
                           ['pickup-or-delivery',
                            'select-delivery-method',
                            '--order_id',
                            '1',
                            '--method',
                            'foodora',
                            '--address',
                            '60 college st'])
    assert result.exit_code == 0
    assert 'Delivery has been selected' in result.output
