#1 Create a string variable "name" with you full name .Print

# a. 1st chracter
# b. 2nd chracter
# c. The length of string

# name = "Guddiya"
# print(name[0]) # print 1st character
# print(name[-1]) # print 2nd character
# print(len(name))

# 2. concatinate two strings "Hello" and "World" with a space between

# a = "Hello"
# b = "World"

# print(a + " " + b)


# 3 STRING SLICING AND iNDEXING 

# a.Given text "Python Programming" do the following

# b. print the first 6 characters

text = "Python Programming"

print(text[0:6])

# c. Print the last 6 characters

print(text[-6:])
# d. print  every second character of the string

print(text[::2])

# e.Reverse the string text using slicing

print(text[::-1])
 
#  @ STRING METHONDS and FUNCTIONS

# 4. Take the string " I 

# 1.Using format() , create a sentance
# love python programming "

#  @ STRING METHONDS and FUNCTIONS

# 4. Take the string " I 
texe1 = " I love python Programming  "

#   a. Remove the extera spaces from both ends

print(texe1.strip())

# Convert into title it to title case

print(texe1.title())

# Count how many times "o" appears

print(texe1.count("o"))

# 2. Check if the string "123abc" alphanumeric

str1 = "123abc"
if str1.isalnum() :
    print("Yes this string is alphanumeric")
else :
    print("No this string is not alphanumeric")    
 

# @ STRING FORMATTING AND f-strings

# 6.Using format() , create a sentance

# My name is johan and I am 25 years old
# by passing "johan" and 25 as variables

name = "johan"
age = "25"
 
print("My name is \"{}\"".format(name))
print("My age is \"{}\"".format(age) )

a = "Guddiya"
b = "25"

print(f"My name  is {a} and My age is {b}")


# @ STRING MANIPULATING CHALANGES

# 7. Given sentences = "Coding in python is fun" , replace "fun" with awosome and print it

Sentence = "Coding in python is fun"

new = Sentence.replace("fun","awsome")
print(new)
print(Sentence.replace("fun","awosome"))

# 8. Find the index of the word "python" in sentence

print(Sentence.index("python"))

# 9. Convert the entire sentesnce into uppercase

print(Sentence.upper())

# 10. Write a program that count how many "vowels" in that sentances

sum = 0
vowels = ['a','e','i','o','u']

for char in Sentence:
    if(char in vowels):
        sum += 1
        
        
print(f"There are {sum} vowels in this Sentence")       


# 11. Take a user input and check if it is palidrom (same fforward and backwoard)

string2 = "level"

if(string2 == string2 [::-1]):
    print("Strin2 is palidrom")
else:
    print("String2 is not palidrom")    