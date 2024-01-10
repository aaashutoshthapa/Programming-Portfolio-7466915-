# Modify your program again so that the chosen password cannot be one of a list of
# common passwords, defined thus:
# BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']  # List of common passwords

first_password=input("Enter a passowrd: ") # Prompts user to enter first password
if 8<= len(first_password) <=12:           # Checks weather the length of password is in the between 8 to 12 (inclusively) 
    if first_password not in BAD_PASSWORDS: # checks weather the first password is list of common passwords
        second_password=input("Re-enter your password: ")
        if first_password == second_password: #checks weather first_password and second_password are same 
            print("Password set")
        else:
            print("Error: password don't match")
    else:
        print("Error: this is a common password.")
else:
    print("Password length should be between 8 to 12")

