'''
Python Operators
Operators are used to perform operations on variables and values.

In the example below, we use the + operator to add together two values:

print(10 + 5)

Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators
'''
# Arithmetic Operators
'''
Arithmetic operators are used with numeric values to perform common mathematical operations:
Operator	Name	    Example
+	      Addition	   x + y
-	    Subtraction    x - y
*	   Multiplication	 x * y
/	     Division	     x / y
//	Floor division	 x // y
%       Modulus	     x % y
**	Exponentiation	 x ** y
'''
""" x = 10
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y)
print(x%y) # output is 1 because remainder is 1
print(x**y) """
# Python Assignment Operators
"""
Assignment operators are used to assign values to variables:

Operator   	Example    	Same As
=	           x = 5	     x = 5
+=	         x += 3	     x = x + 3
-=	         x -= 3	     x = x - 3
*=	         x *= 3	     x = x * 3
/=	         x /= 3	     x = x / 3
%=	         x %= 3	     x = x % 3
//=	         x //= 3	   x = x // 3
**=	         x **= 3	   x = x ** 3
&=	         x &= 3	     x = x & 3
|=	         x |= 3	     x = x | 3
^=	         x ^= 3	     x = x ^ 3
>>=	         x >>= 3   	 x = x >> 3
<<=	         x <<= 3	   x = x << 3
:=	      print(x := 3)	 x = 3
                         print(x)
"""
x = 10
print(x)
x +=3
print(x)
x -=4
print(x)
x *=2
print(x)
x /= 4
print(x)
x %= 2
print(x)
x **= 3
print(x)
x //= 3
print(x)
a = 10
a &= 5
print(a)
print(bin(a))
a |= 5
print(a)
print(bin(a))
b = 5
b ^= 3
print(b)
b = 5
b >>=2
print(b)
b = 5
b <<=3
print(b)
print(x:=5)
# Define a function that converts a decimal number to binary
def decimal_to_binary(num):
    # Base case: if the number is greater than or equal to 1
    if num >= 1:
        # Recursively call the function with the integer division of num by 2
        decimal_to_binary(num // 2)
    # Print the remainder when num is divided by 2, without a newline
    # This prints the binary digits in reverse order due to recursion
    print(num % 2, end='')

# Initialize a variable 'y' with the decimal value to be converted
y = 5

# Call the function and pass the decimal value as the argument
decimal_to_binary(y)  # Output will be the binary representation of 5 (101)


# Python Comparison Operators

""" Comparison operators are used to compare two values:
Operator	 Name	   Example
   ==	     Equal	 x == y
   != 	Not equal	 x != y
   >	 Greater than	  x > y
   <	   Less than	  x < y
   >=	Greater than or equal to	x >= y
   <=	Less than or equal to	x <= y """
print()
x = 5
y = 3
print(x == y) # False because x and y is not equal
print(x != y) # True because x and y is not equal
print(x > y) # True because x is greater than y
print(x < y) # True because y is less than x
print(x >= y) # True because x is greater than y
print(x <= y) # False because x is not less or equal to y

# Python Logical Operators
""" Logical operators are used to combine conditional statements:
Operator	Description	                                                   Example
  and 	  Returns True if both statements are true	                 x < 5 and  x < 10
  or	    Returns True if one of the statements is true	             x < 5 or x < 4
  not	    Reverse the result, returns False if the result is true	   not(x < 5 and x < 10) """
x = 10
print(x>7 and x<13) # True as you know
print(x>7 or x<9) # True because 1 condition is satisfied
print(not(x>7 or x<9)) # False because 1 condition is satisfied it returns True but (not) operator converts it to False
print(not(x>7 or x<13)) # False because both conditions are satisfied it returns True but (not) operator converts it to False

# Python Identity Operators
""" Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
Operator	Description	                                              Example
  is 	    Returns True if both variables are the same object	      x is y
is not	  Returns True if both variables are not the same object	  x is not y """
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True because it located same memory place
print(x is y) # False because it located different memory place
print(x == y) # True because they have same values
print(x is not y) # True because it located different memory place therefore it returns False then (not) operator converts it to True

# Python Membership Operators
""" Membership operators are used to test if a sequence is presented in an object:

Operator	                                 Description	                                     Example
  in 	    Returns True if a sequence with the specified value is present in the object	      x in y
 not in	  Returns True if a sequence with the specified value is not present in the object	 x not in y """
x = ['apple', 'banana']
print("Apple" in x) # False because python is case sensetive
print("apple" in x) # True because list has (apple) item
print("cherry" in x) # False because list has not (apple) item
print("cherry" not in x) # True because list has not (apple) item

# Python Bitwise Operators
""" Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y
|	OR	Sets each bit to 1 if one of two bits is 1	x | y
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
~	NOT	Inverts all the bits	~x
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
print(bin(6 & 3)) # if both site is 1 it will be 1 otherwise it returns 0
print(bin(6 | 3)) # if one site is 1 it will be 1 otherwise it returns 0
print(bin(6 ^ 3)) # if one site is 1 it will be 1, but both site is 1 it will be 0 otherwise it returns 0
print(bin(~3)) # 0 becomes 1 and 1 becomes 0
print(bin(6 << 3))
print(bin(6 >> 3))
