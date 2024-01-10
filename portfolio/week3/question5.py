# Modify your program a final time so that it executes until the user successfully
# chooses a password. That is, if the password chosen fails any of the checks, the
# program should return to asking for the password the first time.

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']   # List of common passwords

while True:   # Loop indefinitely until a valid password is entered or criteria are met
    first_password=input("Enter a passowrd: ")    # Prompt the user to enter the first password
    
    # Check if the length of the password is between 8 and 12 characters (inclusive)
    if 8<= len(first_password) <=12: 
        if first_password not in BAD_PASSWORDS:  # Check if the entered password is not in the list of common passwords
             # If the password is not a common one, prompt the user to re-enter the password
            second_password=input("Re-enter your password: ")
           
            if first_password == second_password:   # Check if the first and second passwords match
                print("Password set")  # If both passwords match, print a message confirming successful password setting and break the loop
                break
            else:
                print("Error: password don't match")
        else:
            print("Error: this is a common password.")
    else:
        print("Password length should be between 8 to 12")
