'''
Python has a set of built-in methods that you can use on strings.
'''
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
print(a.lower())

'''
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
'''
# The strip() method removes any whitespace from the beginning or the end:
b = "      Hello, World!      "
print(b.strip()) # output is "Hello, World!"

# The replace() method replaces a string with another string:
print(a.replace("W", "V"))
print(a.replace("World", "Dunyo"))

'''
The split() method returns a list where the text between the specified separator becomes the list items.
'''
# The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']
print(a.split("e")) # returns ['H', 'llo, World!']