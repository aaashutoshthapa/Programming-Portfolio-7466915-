# Import necessary modules for file operations and user management
import sys
import adduser, deluser, login, passwd


try:
        
    cmdline_arguent = sys.argv[1]   # Get the command-line argument specifying the file to be accessed

    while True:  # Main loop for user interaction
        choice = None
                
        choice  = input("\python@python-user:~$  ").strip()  # Prompt for user input with a custom shell-like prompt
        
        # Execute the appropriate action based on user's choice
        if choice.lower() == "adduser":
            adduser.add_user(cmdline_arguent)
        
        elif choice.lower() == "login":
            login.login_credentials(cmdline_arguent)
            
        elif choice.lower() == "passwd":
            passwd.change_password(cmdline_arguent)
            
        elif choice.lower() == "deluser":
            deluser.delete_user(cmdline_arguent)
            
        elif choice.lower() == "help": # Display information about available commands
            print("\n' adduser ' - Creates a new user")
            print("' login ' - Check for login")
            print("' passwd ' - Change Password")
            print("' deluser ' - Deletes existing user")
            print("' exit ' - exits the command center\n")
            
        elif choice.lower() == "exit":
            break # Break out of the loop to exit the program
        
        else:  
            print(f"\nInvalid Command:{choice} \nPlease try again.\n")  # Display an error message for invalid commands

except FileNotFoundError:   # Handle the case where the specified file does not exist
    print("\nThe file you are trying to access does not exist.")


            
        
        
        
        

                
