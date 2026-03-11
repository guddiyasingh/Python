def average(a,b,c):
    d = (a+b+c)/2
    return d

o1 = average(2,4,3)
o2 = average(6,7,8)

print(o1)
print(o2)

# functions Arguments

def add(a,b):
    return a+b
c= add(2,3)
print(c)


# lamda function

square = lambda x: x*x
sum = lambda x,y: x+y

print(square(3))
print(sum(3,32))



# fabinisies series

def fib(n):

    if(n == 0 or n == 1):
        return n
    
    return fib(n-2) + fib(n-1)

print(fib(6))


def add(a,b):
    return a+b

# Example Uses

num1 =20
num2 = 30

print("Sum:", add(num1,num2))

def sub(a,b):
    return a-b

a =3
b=4

print("Sub:", sub(a,b))



# Two types of Modules
# Builts in modules
# External modules

import random  
num = random.randint(1, 10)
print(f"Random integer between 1 and 10: {num}")
fruits = ["Java", "C", "C++", "Python"]
chosen_fruit = random.choice(fruits)
print(f"Randomly chosen language: {chosen_fruit}")


import math
import os
# import mymodule
import requests

print(math.sqrt(16))
# mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)