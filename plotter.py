# This imports the main plotting engine.
import matplotlib.pyplot as plt

# These are the actual drawing tools
from matplotlib.patches import Rectangle as PatchRectangle
from matplotlib.patches import Circle as PatchCircle

# import the shape classes so we can check what type of shape we're being asked to draw.
from shape import Shape

# Import the 2D Shape classes
from circle import Circle
from rectangle import Rectangle


class Shape2dPlotter:
    """
    A class to plot multiple 2D shapes (Circles and Rectangles)
    on a single set of axes using matplotlib.
    """

    def __init__(self):
        # Create a figure and axes for plotting
        self.fig, self.ax = plt.subplots()
        # Ensures circles are not ellipses
        self.ax.set_aspect("equal", "box")
        # This simply adds a grid to the background, like graph paper.
        self.ax.grid(True)
        """
        This list is the "Composition" part.
        t creates an empty list inside the plotter object. 
        This list will "has-a" collection of all the shapes you add.
        """
        self.shapes = []

    def add_shape(self, shape: Shape):
        """
        Adds a 2D shape (Circle or Rectangle) to the plotter's list.
        It will ignore 3D shapes.
        """
        # We only want to plot 2D shapes
        if isinstance(shape, (Circle, Rectangle)):
            self.shapes.append(shape)
        else:
            print(f"Error: Skipping 3D shape {type(shape).__name__}")

    def plot_shapes(self):
        """
        Draws all added shapes onto the plot.
        """
        if not self.shapes:
            print("No shapes to plot.")
            return

        min_x, max_x = 0, 0
        min_y, max_y = 0, 0

        # Loop through all the shapes in our list
        for shape in self.shapes:
            # This is Polymorphism. The code changes its behavior based on the object's type.
            if isinstance(shape, Circle):
                # Matplotlib's Circle patch takes the center (x,y) and radius
                patch = PatchCircle(
                    (shape._x, shape._y),
                    radius=shape._radius,
                    edgecolor="blue",
                    facecolor="lightblue",
                    alpha=0.6,
                )

                # Update boundaries for plot scaling
                min_x = min(min_x, shape._x - shape._radius)
                max_x = max(max_x, shape._x + shape._radius)
                min_y = min(min_y, shape._y - shape._radius)
                max_y = max(max_y, shape._y + shape._radius)

            # If the shape is a Rectangle, it runs this code instead.
            elif isinstance(shape, Rectangle):
                """
                Rectangle class stores the CENTER (x,y).
                Matplotlib's patch needs the BOTTOM-LEFT corner (x,y).
                """
                bottom_left_x = shape._x - (shape._width / 2)
                bottom_left_y = shape._y - (shape._height / 2)

                # It creates the rectangular "stamp" using the converted coordinates.
                patch = PatchRectangle(
                    (bottom_left_x, bottom_left_y),
                    width=shape._width,
                    height=shape._height,
                    edgecolor="red",
                    facecolor="lightcoral",
                    alpha=0.6,
                )

                # Update boundaries for plot scaling
                min_x = min(min_x, bottom_left_x)
                max_x = max(max_x, bottom_left_x + shape._width)
                min_y = min(min_y, bottom_left_y)
                max_y = max(max_y, bottom_left_y + shape._height)

            # Add the patch to the axes
            self.ax.add_patch(patch)

        # Adjust plot limits to fit all shapes nicely
        padding = 2
        self.ax.set_xlim(min_x - padding, max_x + padding)
        self.ax.set_ylim(min_y - padding, max_y + padding)

    def show_plot(self):
        """
        Displays the final plot window.
        """
        self.plot_shapes()
        plt.show()
