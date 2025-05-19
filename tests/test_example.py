"""
Example test file to demonstrate testing with UV.

Run tests using:
    uv run -m pytest
"""

import pytest
from package_name.example import hello_world


def test_hello_world(capsys):
    """Test that the hello_world function prints the expected output."""
    hello_world()
    captured = capsys.readouterr()
    assert "Hello from UV Python Template!" in captured.out
    assert "This code is running through UV!" in captured.out
