import codecs # Encrypts the data entered 
import getpass # Hides the value enter from the user point of view



def delete_user(cmdline_argument):
        
    """
    Delete a user from a file containing user credentials.

    Parameters:
    - cmdline_argument (str): The path to the file containing existing user credentials.

    Returns:
    None

    This function prompts the user to enter their username and password.
    It then checks if the entered username and password match any user in the specified file.
    If a match is found, it removes the corresponding user from the file. If no match is found,
    an error message is displayed.

    """
    
    username = input(">>>Enter username: ")   # Prompt the user to input their username.
    password = getpass.getpass(">>>Enter your password: ")  # Prompt the user to input their password securely.
    encoded_password = codecs.encode(password, "rot13")  # Encode the password using the ROT13 algorithm.
    
    lines = []  # Initialize an empty list to store lines from the file.
    delete_user = False # Initialize delete_user as false
    
    with open(cmdline_argument, "r") as file:
        for line in file:
            new_line = line.split(":") # Split the line by colon (":") to extract information
            
            if len(new_line) >= 3 and new_line[0] == username: # Check if the line contains at least three elements and the first element matches the provided username
                
                if new_line[2].strip() == encoded_password: # Check if the provided encoded password matches the stored password
                    
                    delete_user = True  # Set delete_user flag to True if credentials are correct
                else:
                    print("Error: Wrong password. Check your password and try again.")
            else:
                lines.append(line)  # If the line does not match the specified username, add it to the lines list
    
    if delete_user:  # If delete_user flag is True, update the file to exclude the specified user
        with open(cmdline_argument, "w") as new_file:
            for line in lines:
                new_file.write(line)
        print(f"\n{username} Deleted Successfully\n")
    else:
        print(f"Error: Wrong username or password for {username}. User not deleted.")
