# Variables is like a box you can store anything inside of it --> formal way(Variables are containers for storing data values)
# Python do not have any specific type you can easly store any data you want and then it will automatically declare them
# you can check Variables data type using type()
# type int --> Integer (number)
number = 4
print(number)
print(type(number))
# type str --> String (letter)
letter = "Word"
print(letter)
print(type(letter))
# type float --> Float (a number that has a decimal place)
decimalNumber = 3.7
print(decimalNumber)
print(type(decimalNumber))
# type bool --> Boolean (it is returning True or False)
isTrue = True
print(isTrue)
print(type(isTrue))
# or you can assing (casting) values to variables
x = int(3)
print(type(x))
y = str(3)
print(type(y))
z = float(3)
print(type(z))
print(x,y,z)
# When you declaring String you can use " " or ' ' quotes but do not mix them in you code choose which is good for you and use it everwere is you mix them python or also other programmer will confuse
stringDecleration = "This is valid"
stringDecleration = 'This is also valid'
# Python concept is top-down you can change variable value after assign it like
s = 10
# now value is int 10
s = "Jhon"
# now value is str Jhon
print(s) # this will print Jhon
# Python is Case-Sensitive a and A are different
a = "Jhon"
A = "Doe"
# A will not overwrite a
print(a)
print(A)


# Variable Names can have short names like (x, y, z) but i will recommend to use descriptive name like (carName, studentId, myGpa)
'''
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''
# example
'''
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''
# these are below incorrect
'''
2myvar = "John"
my-var = "John"
my var = "John"
'''


# multi word variables have common 3 types of techniques
# Camel Case
myVariableName = "John"
# Pascal Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"
# remember that (age, Age, AGE) are 3 different variable names
