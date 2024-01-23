import codecs # Encrypts the data entered 
import getpass # Hides the value enter from the user point of view

def login_credentials(cmdline_arguments):
    
    """
    Authenticate user credentials by checking them against a file containing user information.

    Parameters:
    - cmdline_arguments (str): The path to the file containing existing user credentials.

    Returns:
    None

    This function prompts the user to enter their username and password.
    It then checks if the entered username and password match any user in the specified file.
    If a match is found, it prints a success message. If no match is found,
    an error message is displayed.
    """   
    
    with open(cmdline_arguments, "r") as flie:
        lines = flie.readlines() # Makes a single list of the file but will make each line into one element 

    username = input("\n>>>Enter your username: ")
    password=getpass.getpass(">>>Enter ypur password: ")
    encripted_password= codecs.encode(password, "rot13")
    
    user_found=False
    # Initially, the user_found flag is set to be False
    
    for i in lines:   # Iterating through each line in the 'lines' list.
        
        line= i.strip().split(":")
        # Stripping any leading/trailing spaces and splitting the line by ':' to extract username, password.
        
        if username == line [0] and encripted_password == line[2]:    
            print ("Login Successful! Welcome back {0}".format(username))
            user_found=True
                
    if user_found== False:
        print("\n User not found or wrong password!! \nPlease check your credentials and try again!!")
    