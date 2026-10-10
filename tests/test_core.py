from ridhun.cli import main
from ridhun.core import greet


def test_greet_default():
    assert greet() == "Hello, world!"


def test_greet_name():
    assert greet("Ridhun") == "Hello, Ridhun!"


def test_cli(capsys):
    assert main(["Claude"]) == 0
    assert capsys.readouterr().out == "Hello, Claude!\n"
