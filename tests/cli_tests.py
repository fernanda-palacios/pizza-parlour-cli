from click.testing import CliRunner
from cli import cli

def test_see_full_menu():
  runner = CliRunner()
  result = runner.invoke(cli, ['menu', 'see-full-menu'])
  assert result.exit_code == 0
  assert 'menu:' in result.output


def test_item_price():
  runner = CliRunner()
  result = runner.invoke(cli, ['menu', 'item-price', '--item_id', '1'])
  assert result.exit_code == 0
  assert 'price:' in result.output


def test_create_order():
  runner = CliRunner()
  result = runner.invoke(cli, ['order', 'create-order'])
  assert result.exit_code == 0
  assert 'Order has been created. Order Id:' in result.output

def test_add_item_to_order():
  runner = CliRunner()
  result = runner.invoke(cli, ['order', 'add-item-to-order', '--order_id', '1', '--item_id', '2'])
  assert result.exit_code == 0
  assert 'Added item to order' in result.output

