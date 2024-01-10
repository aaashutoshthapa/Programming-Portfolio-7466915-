# Write a program that simulates the way in which a user might choose a password.
# The program should prompt for a new password, and then prompt again. If the two
# passwords entered are the same the program should say "Password Set" or
# similar, otherwise it should report an error.

first_password=input("Enter a passowrd: ")
second_password=input("Re-enter your password: ")
# Prompts user to enter first passsword and second password 

if first_password == second_password: # checking weather first_password and second_process are equal
    print("Password set")
else:
    print("Error: password don't match")