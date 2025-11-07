# I need this to get math.pi
import math

# Import Paren's class
from geometry import Geometry


class Sphere(Geometry):
    """
    A Sphere shape, inheriting from the Geometry class.
    It implements its own volume and surface area.
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, radius: float = 1):
        # Call the parent (Geometry) to set up x, y, and z
        super().__init__(x, y, z)

        # Handle the Sphere attribute: radius
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be numeric.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")

        self._radius = float(radius)

    @property
    def volume(self) -> float:
        """Calculates the volume of the sphere."""
        return (4 / 3) * math.pi * (self._radius**3)

    @property
    def surface_area(self) -> float:
        """Calculates the surface area of the sphere."""
        return 4 * math.pi * (self._radius**2)

    # Operator Overloads

    def __eq__(self, other: object) -> bool:
        """Checks for equality (==)."""
        # Two spheres are equal if their radii are the same.
        return isinstance(other, Sphere) and math.isclose(self._radius, other._radius)

    def __repr__(self) -> str:
        """Official string representation (for developers)."""
        return f"Sphere(x={self._x}, y={self._y}, z={self._z}, radius={self._radius})"
