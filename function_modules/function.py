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