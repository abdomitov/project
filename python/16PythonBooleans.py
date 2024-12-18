print("Booleans represent one of two values: True or False.")
'''
In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
'''
print(10 > 9) #True
print(10 == 9) #False
print(10 < 9) #False
# When you run a condition in an if statement, Python returns True or False:
a = 13
b = 91
if b > a: #it will check if b greater than a it will give us True value and "b is greater than a" this block of code working
  print("b is greater than a")
else: #if first condition if (b>a) returns False "b is greater than a" this block of code will work
  print("a is greater than b")

# The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello")) #True because it has str value
print(bool(15)) #True because it has int value
print(bool("")) #False because it does not have any value
print(bool()) #False because it does not have any value
# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

'''
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
'''
# The following will return True:

print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
# The following will return False:

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# You can create functions that returns a Boolean Value: #we will talk about functions later
def myFunction() :
  return True

print(myFunction())

# You can execute code based on the Boolean answer of a function:
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

Example
Check if an object is an integer or not:
"""
print(isinstance(200, int))
print(isinstance("200", int))
