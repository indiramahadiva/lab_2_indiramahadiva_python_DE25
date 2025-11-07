# for comparing float(equality) => math.isclose()
import math
from geometry import Geometry  # Import 3D blueprint (Geometry)


class Cube(Geometry):
    """
    A Cube Shape, inheriting from the Geometry class.
    It implements its own volume and surface area.
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, side: float = 1):
        # Call the parent (Geometry) to set up x, y, and z
        super().__init__(x, y, z)

        # Handle the Cube attribute: side
        if not isinstance(side, (int, float)):
            raise TypeError("Side must be numeric.")
        if side <= 0:
            raise ValueError("Side must be positive.")

        self._side = float(side)

    @property
    def volume(self) -> float:
        """Calculates the volume of the cube."""
        return self._side**3

    @property
    def surface_area(self) -> float:
        """Calculates the surface area of the cube."""
        return 6 * (self._side**2)

    # Operator Overloads
    def __eq__(self, other: object) -> bool:
        """Checks for equality (==)."""
        # Two cubes are equal if their sides are the same.
        return isinstance(other, Cube) and math.isclose(self._side, other._side)

    def __repr__(self) -> str:
        return f"Cube(x={self._x}, y={self._y}, z={self._z}, side={self._side})"
