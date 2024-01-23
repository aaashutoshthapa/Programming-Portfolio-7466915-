import codecs  # Encrypts the data entered 
import getpass  # Hides the value enter from the user point of view

def change_password(cmdline_argument):
    
    """
    Change the password for a user in a file containing user credentials.

    Parameters:
    - cmdline_argument (str): The path to the file containing existing user credentials.

    Returns:
    None

    This function prompts the user to enter their username and current password.
    It then checks if the entered username and password match any user in the specified file.
    If a match is found, it prompts the user to enter a new password and updates the file accordingly.
    If no match is found, an error message is displayed.

    """
    
    
    file = open(cmdline_argument, "r")  # Open the file specified in the command-line argument in read mode
    lines = file.readlines()  
    file.close()
        
    username = input(">>>Enter username: ")  # Get username and password from user input
    password = getpass.getpass(">>>Enter your password: ")
    encrypted_password = codecs.encode(password, "rot13")
        
    user_found = False  # Flag to check if the user is found in the file
        
    with open(cmdline_argument, "w") as newfile: # Open the file in write mode to update it
        for line in lines: 
            # Split the line by colon (":") to extract information
            data = line.split(":")
            username_check = data[0]
            full_name = data[1]
            password_check = data[2].strip()
                
            if username == username_check: # Check if the entered username matches the one in the file
                user_found = True
    
                if encrypted_password == password_check: # Check if the entered password matches the stored password
                    new_password = getpass.getpass(">>>Enter new password: ")
                    encrypted_new_password = codecs.encode(new_password, "rot13")
                        
                    if encrypted_new_password != encrypted_password: # Check if the new password is different from the old one
                        confirm_password = getpass.getpass(">>>Re-enter your new password: ")
                        encrypted_confirm_password = codecs.encode(confirm_password, "rot13")
                            
                        if encrypted_new_password == encrypted_confirm_password:  # Check if the confirmation matches the new password
                            newfile.write(f"{username_check}:{full_name}:{encrypted_new_password}\n")  # Write the updated information to the file
                            print(f"{username_check} your password has been successfully changed.")
                            
                        else:
                            print("New password cannot be same as old password.\nPlease TRY AGAIN!!")
                            newfile.write(line) 
                            return   # Return to avoid further processing
                                
                    else:
                        print("Error: Old password and new password cannot be the same.\nPlease TRY AGAIN!!")
                        newfile.write(line)
                        return   # Return to avoid further processing
                            
                else:
                    print("Error: Please enter correct password.\nPlease TRY AGAIN!!")
                    newfile.write(line)
                    return   # Return to avoid further processing
                        
            else:
                newfile.write(line)  # Write the line back to the file if the username doesn't match
                    
    if not user_found:  # If the user was not found in the file, display an error message
        print("\nUser not found!\nPlease try again.") 
            
    




            
            
    

