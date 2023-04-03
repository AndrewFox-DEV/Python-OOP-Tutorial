import copy
from math import *

class Rectangle:
    # It must necessarily be the first instruction of the class
    '''RECTANGLE CLASS\n
    Etc..
    '''
    # Define private class attributes and their type
    _base: float
    _height: float

    # METHODS
    # In Python, methods are functions defined inside a class,
    # and are used to manipulate the data attributes of instances of the class.

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

    # Note that we added a copy() method that returns a deep copy of the current
    # Rectangle object using the copy module's deepcopy() function. This creates
    # a new object with the same base and height values as the original, but
    # with a different memory address.
    def copy(self) -> 'Rectangle':
        return copy.deepcopy(self)

    # We call the method to render class attributes of the object
    # (or instance) with getters; one tip, use the f-string, as I
    #  wrote the string is to create a clean and nice to view output
    def __str__(self) -> str:
        return f'Rectangle: {{\n\tb: {self.get_base()}\n\th: {self.get_height()}\n}}'
    
    # The __eq__() method checks if the object passed as parameter other
    # is an instance of the class Rectangle and if the value of the base
    # and height of the current object (self) is equal to the corresponding
    # values of the other object (__other) . If the two objects are considered
    # equal, the method returns True, otherwise it returns False.
    def __eq__(self, __other: object) -> bool:
        if self is __other:
            return True
        if not isinstance(__other, Rectangle):
            return False
        return self._base == __other._base and self._height == __other._height

    # The __hash__() method returns a hash value of the tuple containing
    # the base and height values of the current object.
    def __hash__(self) -> int:
        return hash((self._base, self._height))
    
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
    def get_base(self) -> float:
        return self._base
    
    def set_base(self, base: float) -> None:
        self._base = base
        
    def get_height(self) -> float:
        return self._height

    def set_height(self, height: float) -> None:
        self._height = height
    
    # STATIC METHOD DECORATOR AND CLASS METHOD DECORATOR
    # @staticmethod and @classmethod are decorators that
    # can be applied to methods to give them special behavior.
    # STATIC METHOD DECORATOR
    # A method decorated with @staticmethod is a static method,
    # which means it can be called on the class itself without
    # the need for an instance of the class. This method cannot modify
    # the instance state or class state in any way. It is often used as
    # a utility function for the class.
    # CLASS METHOD DECORATOR
    # A method decorated with @classmethod is a class method,
    # which means it is bound to the class and can access
    # and modify the class state. It takes a cls parameter
    # as its first argument, which refers to the class on which the
    # method was called. Class methods are often used as factory
    # methods for creating instances of the class.
    def calculate_perimeter(base: float, height: float) -> float:
        perimeter = (base + height) * 2
        return perimeter
    
    def calculate_area(base: float, height: float) -> float:
        area = base * height
        return area

    # One meaningful method that could use the @staticmethod
    # decorator in the Rectangle class could be calculate_diagonal().
    # This method could calculate the diagonal of a rectangle with
    # the given base and height values. Since this method does not depend
    # on any instance attributes or methods, it could be a static method.
    @staticmethod
    def calculate_diagonal(base: float, height: float) -> float:
        return sqrt(pow(base, 2) + pow(height, 2))
    
    # A meaningful method that could use the @classmethod
    # decoratorin the Rectangle class, we could implement
    # a from_square() method. This method could take the
    # area of ​​a square and create a rectangle with the same
    # area but a different base and height. Since this method
    # needs to access and modify class attributes,
    # it could be a class method.
    @classmethod
    def from_square(cls, side: float) -> 'Rectangle':
        base = side
        height = side / 2
        return cls(base, height)
