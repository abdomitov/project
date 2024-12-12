'''
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
'''

b = "Hello, World!" #do not forget index starts from 0 not 1
print(b[7:11]) #11 is not included output: Worl

# By leaving out the start index, the range will start at the first character:
print(b[:5]) #output is Hello as i mentioned if you scipped starter range it will count from 0 to end index

# By leaving out the end index, the range will go to the end:
print(b[3:]) #output is lo, World! if you scipped end index it takes elements from starter index till the end

# By leaving out both indexes:
print(b[:]) #output is Hello, World! if you scipped both index

# You can use negative indexes to start the slice from the end of the string:
print(b[-5:-2]) #output is orl because !-0, d-1, l-2, r-3, o-4, W-5 but as you know last element is not included