# I use math.isclose() for safe comparisons
import math

# Import our "Shape" parents
from shape import Shape


class Rectangle(Shape):
    """
    A Rectangle shape, inheriting from the base Shape class.
    It implements its own area and perimeter.
    """

    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        """
        Call the parent's __init__ method.
        This tells the Shape parents to handle setting up _x and _y
        """
        super().__init__(x, y)

        # Handle the Rectangle attributes
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("Width and height must be numeric.")
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")

        # Store the width and height as "protected" variables
        self._width = float(width)
        self._height = float(height)

    # The area and perimeter Properties
    @property
    def area(self) -> float:
        """Calculates the area of the rectangle."""
        return self._width * self._height

    @property
    def perimeter(self) -> float:
        """Calculates the perimeter of the rectangle."""
        return 2 * (self._width + self._height)

    # This is the method from The UML that only Rectangle has.

    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square.
        We use math.isclose() for safe float comparison
        """
        return math.isclose(self._width, self._height)

    """
    Operator Overloads.
    Define what == and repr() mean for a Rectangle
    """

    def __eq__(self, other: object) -> bool:
        """
        Checks for equality (==).
        Two rectangles are equal if their width and height
        are the same, regardless of their x,y position.
        """
        if not isinstance(other, Rectangle):
            return False
        # Check if dimensions are the same
        return math.isclose(self._width, other._width) and math.isclose(
            self._height, other._height
        )

    def __repr__(self) -> str:
        return (
            f"Rectangle(x={self._x}, y={self._y}, "
            f"width={self._width}, height={self._height})"
        )
