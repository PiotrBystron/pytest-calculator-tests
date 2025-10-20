"""Unit test suite for a simple calculator module.

Includes:
- basic arithmetic operations (add, subtract, multiply, divide),
- parameterized tests for multiple inputs,
- exception handling (division by zero),
- integration with pytest-html for enhanced reports.
"""

import pytest
from pytest_html import extras as html_extras
from app.calculator import add, subtract, multiply, divide


# -------------------------------------------------------------------------------------
# ADDITION TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (1.5, 2.6, 4.1),  # float numbers
    ],
)
def test_add_various(a, b, expected, record_property, extras):
    """Tests adding different types of numbers (integers and floats)"""

    result = add(a, b)
    record_property("a", a)
    record_property("b", b)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(f"<b>add({a}, {b}) = {result}, expected {expected}</b>"))

    assert result == pytest.approx(expected)


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1e6, 1e6, 2e6),    # very large numbers
        (-1e6, 1e6, 0),     # positive + negative
        (0.0001, 0.0002, 0.0003),  # very small floating point numbers
    ],
)
def test_add_edge_cases(a, b, expected, record_property, extras):
    """Tests addition for extreme and boundary values."""

    result = add(a, b)
    record_property("a", a)
    record_property("b", b)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(f"<b>add({a}, {b}) = {result}, expected {expected}</b>"))

    assert add(a, b) == pytest.approx(expected)


# -------------------------------------------------------------------------------------
# SUBTRACT TEST
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 2, 3),
        (0, 5, -5),
        (-3, -2, -1),
    ],
)
def test_subtract(a, b, expected, record_property, extras):
    """Tests subtracting different values"""

    result = subtract(a, b)
    record_property("a", a)
    record_property("b", b)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(f"<b>subtract({a}, {b}) = {result}, expected {expected}</b>"))

    assert result == pytest.approx(expected)


# -------------------------------------------------------------------------------------
# MULTIPLY TEST
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 12),
        (-2, 3, -6),
        (0, 5, 0),
        (0.9, 0.5, 0.45),
        (0.1, 0.9, 0.09),
    ],
)
def test_multiply(a, b, expected, record_property, extras):
    """Tests various cases of multiplication"""

    result = multiply(a, b)
    record_property("a", a)
    record_property("b", b)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(f"<b>multiply({a}, {b}) = {result}, expected {expected}</b>"))

    assert result == pytest.approx(expected)
    assert isinstance(result, (int, float))


# -------------------------------------------------------------------------------------
# DIVISION TEST
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (-6, 2, -3),
    ],
)
def test_divide_valid(a, b, expected, record_property, extras):
    """Tests division of numbers"""

    result = divide(a, b)
    record_property("a", a)
    record_property("b", b)
    record_property("result", result)
    record_property("expected", expected)
    extras.append(html_extras.html(f"<b>divide({a}, {b}) = {result}, expected {expected}</b>"))

    assert result == pytest.approx(expected)


def test_divide_by_zero():
    """Ensures that dividing by zero raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)


