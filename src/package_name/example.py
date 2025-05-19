"""
Example module to demonstrate a simple Python module in the src-layout pattern.

This file can be run using UV with:
    uv run -m package_name.example
"""


def hello_world():
    """Print a greeting message."""
    print("Hello from UV Python Template!")
    print("This code is running through UV!")


if __name__ == "__main__":
    hello_world()
