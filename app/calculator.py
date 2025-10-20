# app/calculator.py
"""
Simple calculator module used for Pytest skill demonstration.

File contains basic arithmetic functions: add, subtract, multiply, divide,
and a Calculator class for instance-based operations.
"""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Return the difference a - b."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Return the product of a * b."""
    return a * b


def divide(a: Number, b: Number) -> Number:
    """Divide a by b. Raise ValueError if b equals zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b



class Calculator:
    """Simple calculator class for instance-based arithmetic operations."""

    def __init__(self, initial: Number = 0):
        """Initialize the calculator with an optional starting value."""
        self.value = initial

    def add(self, x: Number) -> Number:
        """Add x to the current value and return the result."""
        self.value = add(self.value, x)
        return self.value

    def subtract(self, x: Number) -> Number:
        """Subtract x from the current value and return the result."""
        self.value = subtract(self.value, x)
        return self.value

    def multiply(self, x: Number) -> Number:
        """Multiply the current value by x and return the result."""
        self.value = multiply(self.value, x)
        return self.value

    def divide(self, x: Number) -> Number:
        """Divide the current value by x and return the result."""
        self.value = divide(self.value, x)
        return self.value

    def reset(self) -> None:
        """Reset the calculator value to zero."""
        self.value = 0
