# Modify your previous program so that the password must be between 8 and 12
# characters (inclusive) long.

first_password=input("Enter a passowrd: ")   # Prompt the user to enter the first password
if 8<= len(first_password) <=12:    # Check if the length of the password is between 8 and 12 characters (inclusive)
    
    # If the password length is within the specified range, prompt the user to re-enter the password
    second_password=input("Re-enter your password: ")
    
    
    if first_password == second_password:  # Check if the first and second passwords match
        # If the passwords don't match, print an error message
        print("Password set")
    else:
        # If the passwords don't match, print an error message
        print("Error: password don't match")
else:
    print("Password length should be between 8 to 12")

