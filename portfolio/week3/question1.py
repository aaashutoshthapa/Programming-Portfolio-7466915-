# Modify your greeting program so that if the user does not enter a name (i.e. they
# just press enter), the program responds "Hello, Stranger!". Otherwise it should print
# a greeting with their name as before.



name=input("Enter your name: ")  # Prompt the user to enter their name

if name == "":                   # Check if the entered name is an empty string
    print("Hello, Stranger")  
else:                            # If a name is provided, print a personalized greeting using the entered name
    print(f"Hello, {name}")
