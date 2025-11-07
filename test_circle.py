# Imports the testing framework
import pytest

# To get math.pi, To Use math.isclose()
import math

# Imports the class
from circle import Circle

# I import this to test inequality
from rectangle import Rectangle


# Test __init__
def test_init_normal():
    """Tests the constructor with normal values."""
    c = Circle(x=1, y=2, radius=3)
    assert c._x == 1
    assert c._y == 2
    assert c._radius == 3


def test_init_defaults():
    """Tests the constructor with default values."""
    c = Circle()  # Should be x=0, y=0, radius=1
    assert c._x == 0
    assert c._y == 0
    assert c._radius == 1


# Test Properties
def test_properties():
    """Tests the area and perimeter properties."""
    c = Circle(radius=2)
    # Use pytest.approx for float values
    assert c.area == pytest.approx(math.pi * 4)
    assert c.perimeter == pytest.approx(math.pi * 4)


# Test Operators
def test_equality():
    """Tests the __eq__ (==) operator."""
    c1 = Circle(x=0, y=0, radius=5)
    c2 = Circle(x=10, y=20, radius=5)
    r1 = Rectangle(width=1, height=1)

    assert c1 == c2  # True: Same type and radius
    assert c1 != r1  # True: Different types


def test_comparisons():
    """Tests the <, >, <=, >= operators."""
    c1 = Circle(radius=2)  # Area is ~12.56
    c2 = Circle(radius=3)  # Area is ~28.27

    assert c1 < c2
    assert c2 > c1
    assert c1 <= c2
    assert c2 >= c1
    assert c1 <= c1  # Test equality part


# Test Methods
def test_translate():
    """Tests the translate method."""
    c = Circle(x=5, y=5)
    c.translate(1, -2)  # Move right 1, down 2
    assert c._x == 6
    assert c._y == 3


def test_is_unit_circle():
    """Tests the is_unit_circle method."""
    c_unit = Circle(radius=1)
    c_not_unit = Circle(radius=1.1)
    assert c_unit.is_unit_circle() is True
    assert c_not_unit.is_unit_circle() is False


# Test Error Handling
def test_error_handling():
    """
    Tests that the class correctly raises errors.
    Test TypeError for wrong inputs
    """
    with pytest.raises(TypeError):
        Circle(x="a", y=0)  # wrong x

    with pytest.raises(TypeError):
        Circle(radius="10")  # wrong radius

    with pytest.raises(TypeError):
        c = Circle()
        c.translate("one", "two")  # wrong translate

    # Test ValueError for invalid numbers
    with pytest.raises(ValueError):
        Circle(radius=0)  # Radius must be positive

    with pytest.raises(ValueError):
        Circle(radius=-10)  # Radius must be positive
