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

# 1. Take the string " I love python programming "

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

# 1.Using format() , create a sentance

# My name is johan and I am 25 years old
# by passing "johan" and 25 as variables

