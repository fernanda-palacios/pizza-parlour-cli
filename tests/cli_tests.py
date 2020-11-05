from click.testing import CliRunner
from cli import cli

def test_dots():
  runner = CliRunner()
  result = runner.invoke(cli, ['dots', '--n', '3'])
  assert result.exit_code == 0
  assert '...' in result.output

def test_menu():
  runner = CliRunner()
  result = runner.invoke(cli, ['menu', 'see-full-menu'])
  assert result.exit_code == 0
  assert 'menu:' in result.output