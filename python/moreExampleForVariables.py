# you can assign values to multiple variables
# make sure number of variables must matches number of values
# correct example
x, y, z = 11, "12", 13.0
print(x)
print(y)
print(z)
# incorrect example
'''
x, y, z = 9, 10
'''
# or you can assigne multiple variables to one value
x = y = z = 10
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. You can extract the values into variables. This is called unpacking.
# List example
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# you can print items like this as you know
x = "Python is awesome"
print(x)
# or you can add same values to out them correctly
x = "Python"
y = " is " # simply add space to see more readable
z = "awesome"
print(x + y + z)
x = "Python"
y = "is"
z = "awesome"
print(x + " " + y + " " + z) # or add spaces
print(x, y, z) # or simply use this
x = 10
y = 5.0
print(x, y) # just print values
print(x + y) # this works like mathematical operator
# but be careful
x = "Jhon"
y = 13
# print(x + y) # give you and error
# instead of this you can use opeator below
print(x, y)
# Global variable examples
'''
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
'''

i = "awesome"

def myfunc():
  # if you create a variable with same name as global variable that variable will be local and only used inside of the function
  # example
  i = "fantastic"
  print("Python is " + i)
  # if you want your variable global you can use (global) keyword to make it global
  global j
  j = "Global"
  print("Example of", j)


myfunc()

print("Python is " + i)
print("Example of", j)