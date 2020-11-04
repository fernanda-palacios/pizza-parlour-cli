from click.testing import CliRunner
from cli import cli

def test_sync():
  runner = CliRunner()
  result = runner.invoke(cli, ['dots', '--n', '3'])
  assert result.exit_code == 0
  assert '...' in result.output