'''
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:

age = 36
txt = "My name is John, I am " + age #error
print(txt)
# But we can combine strings and numbers by using f-strings or the format() method!


# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
'''
age = 36
name = "Jhon"
txt = f"My name is {name}, I am {age}, My GPA is {3.7}" #you can use variables(placeholders) and also values
print(txt)

# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which means fixed point number with 2 decimals:
# A placeholder can contain Python code, like math operations:
price = 59
txt = f"The price is {price/23:.2f} dollars"
print(txt)

# and also you can print them without variables(placeholders) like:
print(f"Hello i am {name}, and my age is {age} and i bought apple from store and it costs {price/20:.2f} and my fav num is {13}")