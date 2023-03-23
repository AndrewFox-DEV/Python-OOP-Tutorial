from Rectangle import Rectangle

# Example to create an instance/ object through
# the constructor, which we will use to initialize
# the class attributes
rectangle = Rectangle()
print(rectangle.calculate_area())
# If the method was static we won't use the instance,
# but Rectangle.method(args), so the instance will never
# be created, an example of this is the math module

# We will use the __str__() method to print the class attributes,
# but if it weren't there we would see the class instance
# address in memory

