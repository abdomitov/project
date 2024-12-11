'''
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello"

You can display a string literal with the print() function:
'''
print("Hello")
print('Hello')

# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny')
print('He is called "Johnny"')

# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

a = "Hello"
print(a)

# You can assign a multiline string to a variable by using three quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
print("or")
print(b)

'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''
a = "Hello, World!"
print(a[1]) # output is e because first character has the position 0  programming language counts from 0

# Since strings are arrays, we can loop through the characters in a string, with a for loop

print()
for x in "Apple":  #later we will deep learn about for loop
  print(x)

# To get the length of a string, use the len() function.
a = "Hello, World!"
print(len(a)) #output is 13 space also countable
a = "Hello,   World!"
print(len(a)) #output is 15 space also countable

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt) #output is True we just check if it is in text or not therefore it calls back bool value
print("Free" in txt) #output is False because Python is Case-Sensitive did you remember

# You can Use it with an if statement:  leter we will deeply learn about this
if "free" in txt:
  print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
print("expensive" not in txt) #output is True because we do not have "expensive" word in out txt
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")