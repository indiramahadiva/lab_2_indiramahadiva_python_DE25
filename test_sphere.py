# Imports the test library
import pytest

## I need this to get math.pi
import math

# Import the class to test
from sphere import Sphere

# Import to test inequality
from cube import Cube


# Test __init__
def test_init_normal():
    """Tests the constructor with normal values."""
    s = Sphere(x=5, y=10, z=15, radius=7)
    assert s._x == 5
    assert s._y == 10
    assert s._z == 15
    assert s._radius == 7


def test_init_defaults():
    """Tests the constructor with default values."""
    s = Sphere()  # Should be x=0, y=0, z=0, radius=1
    assert s._x == 0
    assert s._y == 0
    assert s._z == 0
    assert s._radius == 1


# Test Properties
def test_3d_properties():
    """Tests the volume and surface_area properties."""
    s = Sphere(radius=2)
    # Use pytest.approx for float values
    assert s.volume == pytest.approx((4 / 3) * math.pi * (2**3))
    assert s.surface_area == pytest.approx(4 * math.pi * (2**2))


def test_overridden_2d_properties():
    """Tests that 'area' correctly returns 'surface_area'."""
    s = Sphere(radius=3)
    assert s.area == s.surface_area

    # Test that perimeter correctly raises an error
    with pytest.raises(NotImplementedError):
        s.perimeter


# Test Operators
def test_equality():
    """Tests the __eq__ (==) operator."""
    s1 = Sphere(x=0, y=0, z=0, radius=5)
    s2 = Sphere(x=10, y=20, z=30, radius=5)
    c1 = Cube(side=5)

    assert s1 == s2  # True: Same type and radius
    assert s1 != c1  # False: Different types


def test_comparisons():
    """Tests the <, >, <=, >= operators (based on surface_area)."""
    s1 = Sphere(radius=5)  # Surface Area = 4*pi*25 = ~314
    s2 = Sphere(radius=6)  # Surface Area = 4*pi*36 = ~452

    assert s1 < s2
    assert s2 > s1
    assert s1 <= s2


# Test Methods
def test_translate():
    """Tests the overridden translate method."""
    s = Sphere(x=5, y=5, z=5)
    s.translate(1, -2, 3)  # Move x=1, y=-2, z=3
    assert s._x == 6
    assert s._y == 3
    assert s._z == 8

    # Test translating without dz
    s.translate(1, 1)
    assert s._x == 7
    assert s._y == 4
    assert s._z == 8  # z should not change


# Test Error Handling
def test_error_handling():
    """
    Tests that the class correctly raises errors.
    Test TypeError for wrong inputs
    """
    with pytest.raises(TypeError):
        Sphere(z="z")  # wrong z

    with pytest.raises(TypeError):
        Sphere(radius="10")  # wrong radius

    with pytest.raises(TypeError):
        s = Sphere()
        s.translate(1, 1, "two")  # wrong dz

    # Test ValueError for invalid numbers
    with pytest.raises(ValueError):
        Sphere(radius=0)  # Radius must be positive

    with pytest.raises(ValueError):
        Sphere(radius=-10)  # Radius must be positive
