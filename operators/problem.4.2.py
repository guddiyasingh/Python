# Write the program that keep asking the user to enter the password until they correct one

password = "xyz123"

entered_password = input("Enter correct password :")


while (entered_password != password):
    entered_password = input("Wrong password! Try again  enter password: ")

print("success! you are logged in")