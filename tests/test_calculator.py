import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_multiply():
    assert multiply(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == "Error! Division by zero."

def test_add_negative():
    assert add(-2, -3) == -5

def test_multiply_float():
    assert multiply(2.5, 2) == 5.0

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
])
def test_add_param(a, b, expected):
    assert add(a, b) == expected