"""Advanced pytest examples for the Calculator class.

Includes:
- fixture usage for object setup,
- parameterized tests for multiple inputs,
- validation of instance state and reset behavior,
- integration with pytest-html reports.
"""

import pytest
from pytest_html import extras as html_extras
from app.calculator import Calculator, add



# -------------------------------------------------------------------------------------
# FIXTURE EXAMPLE
# -------------------------------------------------------------------------------------
@pytest.fixture
def calculator():
    """Provides a new Calculator instance for each test"""
    return Calculator()


# -------------------------------------------------------------------------------------
# PARAMETRIZED FUNCTION TEST
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize("a,b,c,expected", [
(1, 1, 1, 3),
(2.5, 0.5, 0.5, 3.5),
(-1, -1, -1, -3),
])
def test_add_parametrized(a, b, c, expected, calculator, record_property, extras):
    """Tests the Calculator.add() method with multiple values"""
    calculator.add(a)
    result = calculator.add(b)
    result = calculator.add(c)

    record_property("a", a)
    record_property("b", b)
    record_property("c", c)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>Calculator.add({a}, {b}, {c})</b><br>"
        f"Result: {result}<br>"
        f"Expected: {expected}</div>"
    ))

    assert result == pytest.approx(expected)


# -------------------------------------------------------------------------------------
# CLASS METHOD TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize("add_value, expected", [
    (5, 5),
    (-2, -2),
])
def test_calculator_add_and_reset(add_value, expected, calculator, record_property, extras):
    """Verifies add() updates the value and reset() clears it"""
    result = calculator.add(add_value)
    record_property("initial_value", 0)
    record_property("added_value", add_value)
    record_property("result", result)

    assert result == pytest.approx(expected)

    calculator.reset()
    record_property("after_reset", calculator.value)
    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>Initial value</b> => 0 <br>"
        f"<b>Calculator.add({add_value})</b> => {result}<br>"
        f"<b>After reset:</b> {calculator.value}</div>"
    ))

    assert calculator.value == 0


# -------------------------------------------------------------------------------------
# INITIAL VALUE TESTS
# -------------------------------------------------------------------------------------
@pytest.mark.parametrize("input_value, add_value, expected", [
    (0, 5, 5),
    (10, -2, 8),
])
def test_calculator_add(input_value, add_value, expected, record_property, extras):
    """Tests add() starting from different initial values."""
    calc = Calculator(input_value)
    result = calc.add(add_value)

    record_property("input_value", input_value)
    record_property("add_value", add_value)
    record_property("expected", expected)
    record_property("result", result)
    extras.append(html_extras.html(
        f"<div style='padding:4px;margin:2px;border:1px solid #ccc;border-radius:5px;'>"
        f"<b>Calculator({input_value}).add({add_value})</b><br>"
        f"Result: {result}<br>"
        f"Expected: {expected}</div>"
    ))

    assert result == pytest.approx(expected)