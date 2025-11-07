# lab_2_indiramahadiva_python_DE25

### This project is an implementation of the "Geometry OOP Lab". The primary goal is to use object-oriented programming to build well-structured classes for 2D and 3D geometric shapes.

##### This project is built on OOP principles:

- Inheritance & DRY: A parent Shape class is used to hold all common logic (like position and comparison methods) to avoid repeating code (Don't Repeat Yourself).

- Polymorphism: Child classes (like Circle and Rectangle) override parent methods (like area and perimeter) to provide their own specific implementations.

- Composition: The bonus Shape2dPlotter class "has-a" list of Shape objects, demonstrating a different kind of OOP relationship.

##### 🌟 Features

Task 1:

- Shape Base Class: A single "parent" class that provides:

  - \_x, \_y attributes for position.
  - translate() method for moving the shape.
  - Error handling for all inputs (e.g., TypeError for non-numeric values, ValueError for radius <= 0).

- Polymorphic Methods:

  - **str** (for print()) is defined once in the Shape class and inherited by all children.
  - **repr** is defined separately in each child class to include data (\_radius).

- Read-Only Properties:

  - @property is used for area and perimeter, making them read-only (getters without setters).

- Operator Overloading:

  - **eq** (for ==) is overridden in each child class to compare attributes ( \_radius for Circle).
  - **lt**, **gt**, **le**, **ge** (for <, >, etc.) are defined once in the Shape class to compare all shapes based on their area.

- Methods:
  - Circle class with is_unit_circle() method.
  - Rectangle class with is_square() method.

Task 2: Features

- 3D Shape :

  - A Geometry parent class that inherits from Shape to add \_z and volume/surface_area properties.
  - Cube and Sphere classes that inherit from Geometry and implement the 3D math formulas.

- Unit Tests:

  - A full pytest test suite with separate files (test_circle.py, test_rectangle.py, etc.) for all four shape classes .
  - Tests check all calculations, inheritance, and error handling (using pytest.raises).

- Composition & Plotting:

  - A Shape2dPlotter class that demonstrates composition by holding a list of Shape objects.
  - Uses matplotlib.patches.Circle and matplotlib.patches.Rectangle to draw the 2D shapes on a graph.

##### 📚 External Sources & Concepts Used

- @property Decorator: Used to create read-only getters for area and perimeter, as learned from https://github.com/indiramahadiva/STI_DE_25_indiramahadiva

- math.isclose(): Used for safe float comparisons in **eq** and is_unit_circle, https://www.w3schools.com/python/ref_math_isclose.asp

- Pytest (Task 2):

  - pytest.raises: Implemented to test for TypeError and ValueError, https://docs.pytest.org/en/7.1.x/how-to/assert.html

  - pytest.approx: Implemented to safely test float calculations (like area and volume), as learned from the pytest float comparison docs, https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-floating-point-numbers

- Matplotlib (Task 2):

  - matplotlib.patches: The plotter.py class uses matplotlib.patches.Circle and matplotlib.patches.Rectangle as required by the lab and learned from https://matplotlib.org/stable/api/patches_api.html

  - Coordinate Conversion: The most critical part of the plotter was learning from the Rectangle patch docs that it requires a bottom-left corner coordinate, not a center. This required implementing the conversion logic: bottom_left_x = shape.\_x - (shape.\_width / 2).
