'''
To insert characters that are illegal in a string, use an escape character.

An escape character is a backslash \ followed by the character you want to insert.

An example of an illegal character is a double quote inside a string that is surrounded by double quotes:

You will get an error if you use double quotes inside a string that is surrounded by double quotes:
'''

# txt = "We are the so-called "Vikings" from the north."
'''
To fix this problem, use the escape character \":

Example
The escape character allows you to use double quotes when you normally would not be allowed:
'''
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# \'	Single Quote
txt = "It\'s normal"
print(txt)
# \\	Backslash
txt = "This will insert one \\ (backslash)."
print(txt)
# \n	New Line
txt = "Hello I am Joe.\nThis message shows new line"
print(txt)
# \r	Carriage Return
print("Hello\rWorld!") #output is World! because it first print Hello then it overwrite to them like Instead of H->W, e->o, l->r, l->l, o->d then !
# if you wanna see more understandable
print("Hello\rHi") #output is Hillo firstly it prints Hello then it changes H->H, e->i, l, l, o
# \t	Tab
print("Hello\tWorld!") #insert tab space output is Hello   World!
# \b	Backspace
print("Hello \bWorld!") #This example erases one character (backspace): output is HelloWorld!
# \f	Form Feed
print("Hello \fWorld!")
'''
output is
Hello
      World!
'''
# \ooo	Octal value
print("\110\145\154\154\157 \127\157\162\154\144\41") #output is Hello World! based on ASCII table ,Oct row you can search it from network

# \xhh	Hex value
print("\x48\x65\x6c\x6c\x6f \x57\x6F\x72\x6C\x64\x21") #output is Hello World! based on ASCII table ,Hex row (but do not forget to put x before every num example in table 48 is H but printing it as H you should write as \x48)you can search it from network
