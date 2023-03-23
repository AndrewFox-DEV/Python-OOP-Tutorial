class Rectangle:
    # It must necessarily be the first instruction of the class
    '''RECTANGLE CLASS\n
    Etc..
    '''
    # Define private class attributes and their type
    _base: float
    _height: float

    # Call the constructor method, it's a special method that
    # allows us to define class attributes the value assignment
    # of formal parameters (method arguments)
    # As you can see, the parameters have also been defined with their own type
    # Through the statement "-> DataType", for example, I gonna define the return
    # type of the method, for now, you may as well admit it,
    # but I suggest you follow these best practices
    def __init__(self, base: float, height: float) -> None:
        self._base = base
        self._height = height

    # We call the method to render class attributes of the object (or instance);
    # one tip, use the f-string, as I wrote the string is to
    # make a clean output and nice to display
    def __str__(self) -> str:
        return f'Rectangle: {{\n\tb: {self._base}\n\th: {self._height}\n}}'
    
    # PROPERTY DECORATOR
    # @property is a Python built-in decorator, which is used to give "special"
    # functionality to certain methods and make them act as getters, setters,
    # or deleters when we define properties in a class.
    # GETTERS AND SETTERS?
    # But, what are these getters and setters actually for?
    # For each instance variable, a getter method returns its value,
    # while a setter method sets or updates its value.
    # GETTERS
    # A getter just returns a value, so we just return the class attribute;
    # as a suggestion, put the return of the method as mentioned before.
    # SETTERS
    # As mentioned, a setter is used to set or modify a value, so simply
    # the class attribute will be equal to a value
    # (which will be defined as a method argument)
    # STATICMETHOD DECORATOR
    # The @staticmethod is a built-in decorator that defines a static
    # method in the class in Python. A static method doesn't receive any
    # reference argument whether it is called by an instance of
    # a class or by the class itself. It's not necessary!
    @property
    def get_base(self) -> float:
        return self._base
    
    @property
    def set_base(self, base: float) -> None:
        self._base = base
    
    @property
    def get_height(self) -> float:
        return self._height
    
    @property
    def set_height(self, height: float) -> None:
        self.height = height

    @staticmethod
    def calculate_perimeter(base: float, height: float) -> float:
        perimeter = (base + height) * 2
        return perimeter

    @staticmethod
    def calculate_area(base: float, height: float) -> float:
        area = base * height
        return area