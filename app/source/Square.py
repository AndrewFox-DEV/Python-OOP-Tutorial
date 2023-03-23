from Rectangle import Rectangle

class Square(Rectangle):
    # Call the constructor of the Rectangle class to initialize
    # the base and height attributes with the side length of the square
    def __init__(self, side_length: float) -> None:
        # What is super().__init__() used for?
        # It's a call to the constructor of the parent class, in the specific
        # case of the Square class, its parent class is Rectangle.
        # Basically, when instantiating a Square object with the side length of
        # the square as an argument, super().__init__(side_length, side_length) is
        # called to initialize the base and height attributes of the parent class
        # with the side length of the square itself.
        # This's one of the great features of inheritance, where the child class can
        # inherit the parent class's methods and attributes and also modify or extend them,
        # as in this case.
        super().__init__(side_length, side_length)

    # Method to string for class Square, really similar
    # to how explained for the Rectangle class
    def __str__(self) -> str:
        return f'Square: {{\n\tsquare: {self._base}\n}}'