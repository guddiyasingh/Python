# function and Arguments

# 1. Write a function greet() that prints "Hello python learner" when called

def greet():
    print("Hello python learner")

greet()    



# Write a function squre(num) that returns the squre of given number .
#  Test it with different numbers.

def squre(x):
    return x*x

print(squre(3))
print(squre(2))
print(squre(4))


# B. Function Arguments and Return value

# Write function full name (first_last) that takes name and last name as parametrs and returns 
# as a single 


def full_name(first,last):
    return f"{first} {last}"


print(full_name("jhon", "doe"))


# C.Lambda And functions

# 1. Write a lambda function that adds two numbers

add = lambda x,y: x+y
print(add(1,2))

# 2. create a list [1,2,3,4,5] and use map() with a lambda function their sqaure

x = [1,2,3,4,5]

def squre(x):
    return x*x

result = map(squre,x)
print (list(result))

squre = lambda x: x*x
result = map(squre,x)
print(list(result))

# D.Recursion on python

# 1.Write a recursion function factorial(n) that returns the factorials