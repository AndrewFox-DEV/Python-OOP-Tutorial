from Rectangle import Rectangle

# Example to create an instance/ object through
# the constructor, which we will use to initialize
# the class attributes
rectangle = Rectangle(1, 100)
# If the method was static we won't use the instance,
# but Rectangle.method(args), so the instance will never
# be created, an example of this is the math module

# We will use the __str__() method to print the class attributes,
# but if it weren't there we would see the class instance
# address in memory

# The del keyword is used to delete objects.
# In Python everything is an object, so the del
# keyword can also be used to delete variables,
# lists, or parts of a list etc.
del rectangle

# The object that was created earlier we want to delete!
# So let's use del as a keyword! We use a try-except to
# check if the object actually exists, which it never will!
# Without try-except the output would be that the object has
# not been defined, and therefore has actually been deleted.
try:
    print(rectangle)
except:
    print('The object has been deleted!')
