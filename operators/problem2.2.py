# Write a program using match case that simulates a simple calculator

# 1. Ask the user for two numbers and an operations (+,-,*,/)
# 2. Perform the operations using match case.   


num1 = int (input("Enter first number:"))
num2 = int (input("Enter second number:"))

operation = input("Choose operation: ")

match operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)    
        
("Choose operation")