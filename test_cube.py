# Imports the pytest testing library.
import pytest

# Imports the Circle class, which is the class i am testing in this file.
from cube import Cube

# Import to test inequality
from sphere import Sphere


# Test __init__
def test_init_normal():
    """Tests the constructor with normal values."""
    c = Cube(x=2, y=4, z=6, side=8)
    assert c._x == 2
    assert c._y == 4
    assert c._z == 6
    assert c._side == 8


def test_init_defaults():
    """Tests the constructor with default values."""
    c = Cube()  # Should be x=0, y=0, z=0, side=1
    assert c._x == 0
    assert c._y == 0
    assert c._z == 0
    assert c._side == 1


# Test Properties
def test_3d_properties():
    """Tests the volume and surface_area properties."""
    c = Cube(side=2)
    assert c.volume == 8  # 2*2*2
    assert c.surface_area == 24  # 6 * (2*2)


def test_overridden_2d_properties():
    """Tests that 'area' correctly returns surface_area."""
    c = Cube(side=3)
    assert c.area == c.surface_area

    # Test that 'perimeter' correctly raises an error
    with pytest.raises(NotImplementedError):
        c.perimeter


# Test Operators
def test_equality():
    """Tests the __eq__ (==) operator."""
    c1 = Cube(x=0, y=0, z=0, side=5)
    c2 = Cube(x=10, y=20, z=30, side=5)
    s1 = Sphere(radius=5)

    assert c1 == c2  # True: Same type and side
    assert c1 != s1  # False: Different types


def test_comparisons():
    """Tests the <, >, <=, >= operators (based on area)."""
    c1 = Cube(side=1)  # Surface Area = 6
    c2 = Cube(side=2)  # Surface Area = 24

    assert c1 < c2
    assert c2 > c1
    assert c1 <= c2


# Test Methods
def test_translate():
    """Tests the overridden translate method."""
    c = Cube(x=5, y=5, z=5)
    c.translate(1, -2, 3)  # Move x=1, y=-2, z=3
    assert c._x == 6
    assert c._y == 3
    assert c._z == 8

    # Test translating without dz
    c.translate(1, 1)
    assert c._x == 7
    assert c._y == 4
    assert c._z == 8  # z should not change


# Test Error Handling
def test_error_handling():
    """
    Tests that the class correctly raises errors.
    Test TypeError for wrong inputs.
    """
    with pytest.raises(TypeError):
        Cube(z="a")  # Wrong z

    with pytest.raises(TypeError):
        Cube(side="10")  # wrong side

    with pytest.raises(TypeError):
        c = Cube()
        c.translate(1, 1, "one")  # wrong dz

    # Test ValueError for invalid numbers
    with pytest.raises(ValueError):
        Cube(side=0)  # Side must be positive

    with pytest.raises(ValueError):
        Cube(side=-10)  # Side must be positive
