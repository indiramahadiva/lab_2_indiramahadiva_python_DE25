# Import the Shape.py
from shape import Shape


class Geometry(Shape):
    """
    A base class for 3D shapes Cube, Sphere.
    It inherits from Shape to get x, y, and basic comparisons,
    but adds a z coordinate and 3D-specific properties.
    """

    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        # Call the parent (Shape) to set up x and y
        super().__init__(x, y)

        # Add the new z coordinate and its error handling
        if not isinstance(z, (int, float)):
            raise TypeError("z must be numeric.")
        self._z = float(z)

    @property
    def volume(self) -> float:
        """Read-only property for the volume."""
        raise NotImplementedError("Child class must implement this property")

    @property
    def surface_area(self) -> float:
        """Read-only property for the shape's surface area."""
        raise NotImplementedError("Child class must implement this property")

    @property
    def area(self) -> float:
        """
        Overrides the 2D 'area' property.
        For a 3D shape, 'area' refers to its 'surface_area'.
        """
        # This fulfills the 'area' contract from the Shape class
        return self.surface_area

    @property
    def perimeter(self) -> float:
        """Overrides the 2D 'perimeter' property."""
        # 3D Shapes dont have perimeter.
        raise NotImplementedError("Perimeter is not defined for a 3D shapes")

    def translate(self, dx: float, dy: float, dz: float = 0) -> None:
        """
        Overrides the 2D 'translate' method to include 'dz'.
        """
        # Call the parent (Shape) to handle dx and dy
        super().translate(dx, dy)

        # Handle the new dz translation
        if not isinstance(dz, (int, float)):
            raise TypeError("dz must be numeric.")
        self._z += float(dz)

    def __str__(self) -> str:
        """Overrides the __str__ method for 3D."""
        try:
            volume_str = f"{self.volume:.2f}"
        except NotImplementedError:
            volume_str = "undefined"

        return (
            f"A 3D {type(self).__name__} centered at ({self._x}, {self._y}, {self._z}) "
            f"The volume is {volume_str}."
        )
