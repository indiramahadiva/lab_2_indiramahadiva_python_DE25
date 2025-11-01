# Parent's class
class Shape:
    def __init__(self, x: float = 0, y: float = 0):
        # Error handling for position
        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            raise TypeError("x and y must be numeric.")
        self._x = float(x)
        self._y = float(y)

    @property
    def area(self) -> float:
        """
        Read-only property for the shape's area.
        This will crash if a child class forgets to create its own area
        """
        raise NotImplementedError("Child class must implement this property")

    @property
    def perimeter(self) -> float:
        """Read-only property for the shape's perimeter."""
        # This will crash if a child class forgets to create its own perimeter
        raise NotImplementedError("Child class must implement this property")

    # The translate method, which will move any shape.
    def translate(self, dx: float, dy: float) -> None:
        """Moves the shape by dx and dy."""
        # Error handling as required
        if not (isinstance(dx, (int, float)) and isinstance(dy, (int, float))):
            raise TypeError(f"Translation values 'dx' and 'dy' must be numeric.")
        self._x += float(dx)
        self._y += float(dy)

    def __str__(self) -> str:
        """User-friendly string representation."""
        # add error handling here in case area is not implemented
        try:
            area_str = f"{self.area:.2f}"
        except NotImplementedError:
            area_str = "undefined"

        return (
            f"A {type(self).__name__} centered at ({self._x}, {self._y}) "
            f"with an area of {area_str}."
        )

    """
    Operator Overloads.
    These handle the comparisons <, >, <=, >= 
    """

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area < other.area

    def __le__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area <= other.area

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area > other.area

    def __ge__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area >= other.area
