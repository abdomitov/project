# Python has a set of built-in methods that you can use on strings.

# capitalize() Converts the first character to upper case
example = "hello world".capitalize()  # "Hello world"
print(example)

# casefold() Converts string into lower case
example = "HELLO WORLD".casefold()  # "hello world"
print(example)

# center() Returns a centered string
example = "hello".center(10)  # "  hello   "
print(example)

# count() Returns the number of times a specified value occurs in a string
example = "hello world".count("o")  # 2
print(example)
example = "hello world".count("l")  # 3
print(example)

# encode() Returns an encoded version of the string
example = "hello".encode()  # b'hello'
print(example)

# endswith() Returns true if the string ends with the specified value
example = "hello world".endswith("world")  # True
print(example)
example = "hello world".endswith("ld")  # True
print(example)

# expandtabs() Sets the tab size of the string
example = "h\te\tl\tl\to".expandtabs(4)  # "h   e   l   l   o"

# find() Searches the string for a specified value and returns the position of where it was found
example = "hello world".find("world")  #index of w is 6 therefore it returns 6 beginning of word
print(example)
example = "hello world".find("l")  #be careful it returns first item in this case is 2 other 3 and 9 is not shown
print(example)

# format() Formats specified values in a string
example = "Hello, {}!".format("Alice")  # "Hello, Alice!"
print(example)

# format_map() Formats specified values in a string
example = "Hello, {name}!".format_map({"name": "Lim"})  # "Hello, Alice!"
print(example)

# index() Searches the string for a specified value and returns the position of where it was found
example = "hello world".index("d")  # 10
print(example)

# isalnum() Returns True if all characters in the string are alphanumeric it must be only str or int no space and float allowed or other char like ! @ #
example = "Hello123".isalnum()  # True
print(example)
example = "Hello 23".isalnum()  # False
print(example)
example = "Hello".isalnum()  # True
print(example)
example = "123".isalnum()  # True
print(example)

# isalpha() Returns True if all characters in the string are in the alphabet only str no space, int or float allowed
example = "Hello".isalpha()  # True
print(example)
example = "Hello ".isalpha()  # False
print(example)
example = "123".isalpha()  # False
print(example)

# isascii() Returns True if all characters in the string are ascii characters
example = "Hello".isascii()  # True
print(example)
example = "0123".isascii()  # True
print(example)

# isdecimal() Returns True if all characters in the string are decimals
example = "123".isdecimal()  # True
print(example)
example = "123.0".isdecimal()  # False
print(example)
example = "Hello".isdecimal()  # False
print(example)

# isdigit() Returns True if all characters in the string are digits
example = "123".isdigit()  # True
print(example)
example = "123.0".isdigit()  # False
print(example)

# isidentifier() Returns True if the string is an identifier
example = "variable1".isidentifier()  # True
print(example)
print("isidentifier examples") #by doing this you can check your created variable is valid or not
a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# islower() Returns True if all characters in the string are lower case
example = "hello".islower()  # True
print(example)
example = "helLo".islower()  # False all str must be lowercase
print(example)

# isnumeric() Returns True if all characters in the string are numeric
example = "123".isnumeric()  # True
print(example)
example = "123.0".isnumeric()  # False
print(example)

# isprintable() Returns True if all characters in the string are printable
example = "Hello!".isprintable()  # True
print(example)
txt = "Hello! Are you #1?".isprintable() # True
print(txt)
txt = "Hello! \nAre you #1?".isprintable() # False because we cannot print \n to the screen
print(txt)

# isspace() Returns True if all characters in the string are whitespaces
example = "   ".isspace()  # True
print(example)
example = "   .".isspace()  # False
print(example)

# istitle() Returns True if the string follows the rules of a title
example = "Hello World".istitle()  # True
# The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
print(example)

# isupper() Returns True if all characters in the string are upper case
example = "HELLO".isupper()  # True
print(example)

# join() Joins the elements of an iterable to the end of the string
example = "-".join(["1", "2", "3"])  # "1-2-3"
print(example)
example = " ".join(["1", "2", "3"])  # "1 2 3"
print(example)

# ljust() Returns a left justified version of the string
example = "hello".ljust(10)  # "hello     "
print(example) # in this way it is harder to catch but i will use another way
print(f"{example} you can see this text has more space")

# rjust() Returns a right justified version of the string
example = "hello".rjust(10)  # "hello     "
print(example)

# lower() Converts a string into lower case
example = "HELLO".lower()  # "hello"
print(example)
example = "123".lower()  # "123" no error
print(example)

# lstrip() Returns a left trim version of the string
example = "   hello".lstrip()  # "hello"
print(example)

# rstrip() Returns a right trim version of the string
example = "hello   ".rstrip()  # "hello"
print(example)

# maketrans() Returns a translation table to be used in translations
trans = str.maketrans("abc", "123")
example = "abc".translate(trans)  # "123"
print(example)
trans = str.maketrans("123", "def")
example = "123".translate(trans)  # "def"
print(example)
txt = "Hello Sam!"
print(txt)
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# partition() Returns a tuple where the string is parted into three parts
example = "hello world".partition(" ")  # ("hello", " ", "world")
print(example)

'''
Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
'''
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# replace() Returns a string where a specified value is replaced with a specified value
example = "hello world".replace("world", "there")  # "hello there"
print(example)

# rfind() Searches the string for a specified value and returns the last position of where it was found
example = "hello hello".rfind("hello")  # 6 when we use find() it starts from beginning (left side)
print(example)

# rindex() Searches the string for a specified value and returns the last position of where it was found
example = "hello hello".rindex("hello")  # 6 when we use index() it starts from beginning (left side)
print(example)

# rpartition() Returns a tuple where the string is parted into three parts
example = "hello world 123".rpartition(" ")  # ('hello world', ' ', '123')
print(example)

# rsplit() Splits the string at the specified separator, and returns a list
example = "1,2,3".rsplit(",")  # ["1", "2", "3"]
print(example)

# split() Splits the string at the specified separator, and returns a list
example = "1,2,3".split(",")  # ["1", "2", "3"]
print(example)

# splitlines() Splits the string at line breaks and returns a list
example = "hello\nworld".splitlines()  # ["hello", "world"]
print(example)

# startswith() Returns true if the string starts with the specified value
example = "hello world".startswith("hello")  # True
print(example)
example = "hello world".startswith("ello")  # False because first element is h
print(example)

# strip() Returns a trimmed version of the string
example = "   hello world   ".strip()  # "hello world" it removes whitespaces from beginning and ending
print(example)

# swapcase() Swaps cases, lower case becomes upper case and vice versa
example = "Hello World".swapcase()  # "hELLO wORLD"
print(example)

# title() Converts the first character of each word to upper case
example = "hello world".title()  # "Hello World"
print(example)

# translate() Returns a translated string
trans = str.maketrans("abc", "123")
example = "abc".translate(trans)  # "123"
print(example)
# Replace any "S" characters with a "P" character:
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper() Converts a string into upper case
example = "hello".upper()  # "HELLO"
print(example)

# zfill() Fills the string with a specified number of 0 values at the beginning
example = "42".zfill(5)  # "00042"
print(example)
# Fill the string with zeros until it is 10 characters long:
example = example.zfill(10)
print(example)
