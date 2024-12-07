# --> this is symbol of comment in pyhton when you use it Python will ignore them

#print("This print message is not shown (is not work)")
print("This print message shown (is work)")
# comments often used for explains code or to prevent code executing
# Python is not multiline comment instead of it you can use multiline Sting like example down
'''
This is used
for multiline comment
in python
'''

## remove single comments to test yourself

## correct syntax
if 13 > 10:
  print("13 is greater than 10!")

## incorrect syntax
# if 13 > 10:
# print("13 is greater than 10!")

## space is up to you but do not forget to put at least one otherwise you will get an error
if 13 > 10:
                  print("13 is greater than 10!")

## and one more thing inside of your block every line of code must start with same space like
if 13 > 10:
  print("13 is greater than 10!")
  print("13 is greater than 10!")
## like this
## or if you write code like this below you will face with error

# if 13 > 10:
#   print("13 is greater than 10!")
#         print("13 is greater than 10!")