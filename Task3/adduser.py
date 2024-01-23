import codecs # Encrypts the data entered 
import getpass # Hides the value enter from the user point of view


def add_user(cmdline_argument):
    
    """
    Parameters:
    - cmdline_argument (str): The path to the file containing existing user credentials.

    Returns:
    None

    This function prompts the user to enter their full name, username, and password.
    It then checks if the entered username already exists in the specified file.
    If the username is unique, it encrypts the password using ROT13 and appends the new
    user information to the file. If the username already exists, the user is prompted
    to enter a new username.
    """
    
    with open(cmdline_argument, "r") as file:
        lines = file.readlines() # Makes a single list of the file but will make each line into one element 
        
    print("Enter your credentials below:\n")
    name = input(">>>Enter your full name: ") 
    full_name= name.title()
    user_name= input(">>>Enter your user name:")
    password = getpass.getpass(">>>Enter a password: ")
    encrypted_password = codecs.encode(password, "rot13")
    
    users = []
    for i in lines:
        usr= i.strip().split(":")[0] # Slices the username from the file  and stores on "usr"
        users.append(usr) # This append the value of usr acc to index into user list which was initially empty 
        
    new_user=[]
    if user_name not in users:
        new_user= f"{user_name}:{full_name}:{encrypted_password}\n"
        with open(cmdline_argument, "a") as append_new_user:
            append_new_user.write(new_user)
        print("\nUser created!")
        print(f"User {user_name} added successfully.\n")
    else:
        print("\nUsername already exists")
        print("Please enter new username!")
        
        print("YOU WILL BE REDIRECTED INTO NEW TERMINAL\n")
        
        
        
        
        
   
        
        
    