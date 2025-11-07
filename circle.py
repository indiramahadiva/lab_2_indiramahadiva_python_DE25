# I need this to get math.pi and I use math.isclose() for safe comparisons
import math

# This imports the parent blueprint.
from shape import Shape

"""Circle class inherit from Shape.
It implements its own area and perimeter."""


class Circle(Shape):

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        # Call the parent's __init__ method first
        super().__init__(x, y)

        # error checks, specific to the radius.
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be numeric.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        # Stores the radius data.
        self._radius = float(radius)

    @property
    def area(self) -> float:
        """Calculates the area of the circle."""
        return math.pi * (self._radius**2)

    """The area and perimeter Properties. 
    I am overriding the parent's methods. Instead of raise NotImplementedError, I am providing the real math formulas.
    """

    @property
    def perimeter(self) -> float:
        """Calculates the perimeter of the circle."""
        return 2 * math.pi * self._radius

    # These are methods from the UML that only Circle has.
    def is_unit_circle(self) -> bool:
        """Checks if the circle is a unit circle (radius=1).
        We use math.isclose() for safe float comparison
        """
        return math.isclose(self._radius, 1.0)

    """Operator Overloads 
    Define __eq__ and __repr__ as they are different from the parent
    """

    def __eq__(self, other: object) -> bool:
        """
        Checks for equality (==).Two circles are equal if their
        radii are the same, regardless of their x,y position.
        """
        if not isinstance(other, Circle):
            return False
        return math.isclose(self._radius, other._radius)

    def __repr__(self) -> str:
        return f"Circle(x={self._x}, y={self._y}, radius={self._radius})"
