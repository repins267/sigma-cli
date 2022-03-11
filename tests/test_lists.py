from typing import Counter
import pytest
from click.testing import CliRunner
from sigma.cli.list import list_pipelines, list_targets, list_formats

@pytest.fixture(params=[list_targets, list_pipelines], ids=["targets", "pipelines"])
def cli_list(request):
    cli = CliRunner()
    yield cli.invoke(request.param)

def test_simple_list(cli_list):
    counts = Counter(cli_list.output)
    assert cli_list.exit_code == 0 \
        and len(cli_list.output.split()) >= 5 \
        and counts["|"] >= 6 \
        and counts["-"] >= 40

def test_format_list():
    cli = CliRunner()
    cli_list = cli.invoke(list_formats, ["splunk"])
    counts = Counter(cli_list.output)
    assert cli_list.exit_code == 0 \
        and len(cli_list.output.split()) >= 5 \
        and counts["|"] >= 6 \
        and counts["-"] >= 40