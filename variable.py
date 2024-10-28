name = 'Vanshika'
print(name)

# value = float(str(int(str(float("3.0")))))
# print(value)  # value error invalid literal for int

# value1 = int(str(float("3.29")))
# print(value1) # value error

# value2 = int(float("3.29"))
# print(value2) # 3; type = integer

# value3 = int(str(str("3.0")))
# print(value3) # value error

# value4 = str(str("3.0"))
# print(value4) # 3.0; type = float

# single quotes and double quotes strings are same in python

# legal variable names
''' 
myvar = "Vanshika"
myVar = "Vanshika"
MYVAR = "Vanshika"
myVar1 = "Vanshika"
my_var = "Vanshika"
_my_var = "Vanshika" 
'''

# illegal variable names
''' 
2myvar = "Vanshika"
my-var = "Vanshika"
my var = "Vanshika" 
'''

# Assign multiple values to different variables
''' x, y, z = "Val1", "Val2", "Val3"
print(x, y, z) '''

# Assign one value to different variables
'''
x = y = z = "One For All"
print(x, y, z)
'''

# Unpack a list/collection
'''
list1 = ["v1", "v2", "v3"]
a, b, c = list1
print(a, b, c)
'''

# concatenate two variables
'''
c1 = '3'
c2 = 5
print(c1, c2) # 3 5
#print(c1 + c2) # python can only concatenate str to str not int to str
print(str(c2) + c1) #53
print(str(c2), c1) # 5 3
'''

#print("Before function initialization I am" + v1) # NameError v1 not defined
'''
def myFunc1():
 global v1
 v1 = "Python"
 print(v1) # part of a function because indentation
print(v1) # NameError // not part of a function because at defined at function level

myFunc1()
print("After function initialization I am"+ v1)
'''

'''global x
x = "r"

def myfunc2():
    x = "f"
    print(x)
myfunc2()  # f  '''

# Types of Error
'''
NameError
ValueError
SyntaxError
'''







