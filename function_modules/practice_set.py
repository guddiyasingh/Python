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