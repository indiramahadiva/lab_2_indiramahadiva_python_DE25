import pytest
from rectangle import Rectangle
from circle import Circle  # I import this to test inequality


# Test __init__
def test_init_normal():
    """Tests the constructor with normal values."""
    r = Rectangle(x=1, y=2, width=3, height=4)
    assert r._x == 1
    assert r._y == 2
    assert r._width == 3
    assert r._height == 4


def test_init_defaults():
    """Tests the constructor with default values."""
    r = Rectangle()  # Should be x=0, y=0, width=1, height=1
    assert r._x == 0
    assert r._y == 0
    assert r._width == 1
    assert r._height == 1


# Test Properties
def test_properties():
    """Tests the area and perimeter properties."""
    r = Rectangle(width=10, height=5)
    assert r.area == 50
    assert r.perimeter == 30


# Test Operators
def test_equality():
    """Tests the __eq__ (==) operator."""
    r1 = Rectangle(x=0, y=0, width=10, height=5)
    r2 = Rectangle(x=50, y=50, width=10, height=5)
    r3 = Rectangle(x=0, y=0, width=10, height=6)
    c1 = Circle(radius=1)

    assert r1 == r2  # True: Same type and dimensions
    assert r1 != r3  # False: Different height
    assert r1 != c1  # False: Different types


def test_comparisons():
    """Tests the <, >, <=, >= operators (based on area)."""
    r1 = Rectangle(width=2, height=2)  # Area = 4
    r2 = Rectangle(width=5, height=5)  # Area = 25

    assert r1 < r2
    assert r2 > r1
    assert r1 <= r2
    assert r2 >= r1
    assert r1 <= r1  # Test equality part


# Test Methods
def test_translate():
    """Tests the translate method."""
    r = Rectangle(x=10, y=10)
    r.translate(-5, 2)  # Move left 5, up 2
    assert r._x == 5
    assert r._y == 12


def test_is_square():
    """Tests the is_square method."""
    r_square = Rectangle(width=5, height=5)
    r_not_square = Rectangle(width=5, height=5.1)
    assert r_square.is_square() is True
    assert r_not_square.is_square() is False


# Test Error Handling
def test_error_handling():
    """Tests that the class correctly raises errors."""

    # Test TypeError for wrong inputs
    with pytest.raises(TypeError):
        Rectangle(x="a", y=0)  # wrong x

    with pytest.raises(TypeError):
        Rectangle(width="10")  # wrong width

    with pytest.raises(TypeError):
        r = Rectangle()
        r.translate("one", "two")  # wrong translate

    # Test ValueError for invalid numbers
    with pytest.raises(ValueError):
        Rectangle(width=0, height=10)  # Width must be positive

    with pytest.raises(ValueError):
        Rectangle(width=10, height=-1)  # Height must be positive
