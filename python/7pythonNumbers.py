'''
as you know
There are three numeric types in Python:
int
float
complex
'''
# examples
x = 1    # int
y = 2.8  # float
z = 1j   # complex
# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
x = 1.104504021
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100
print(type(x))
print(type(y))
print(type(z))

# Complex numbers are written with a "j" as the imaginary part:
x = 3j+5
y = 5J
z = -5j

print(type(x))
print(type(y))
print(type(z))

# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
#convert from float to int:
b = int(y)
#convert from int to complex:
c = complex(x)
# convert from float to complex:
f = complex(y)

# Errors
# convert from complex to int:
# d = int(z)
# convert from complex to float:
# e = float(z)
# print(d)
# print(e)
# print(type(d))
# print(type(e))

print(a)
print(b)
print(c)
print(f)


print(type(a))
print(type(b))
print(type(c))
print(type(f))


# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
# every time you rerun the code it will choose numbers automatically between 1 and 9 (10 is not included)
import random # in your code i will recommend to use this kind of import beginning of the code (top of your code)

print(random.randrange(1, 10))
