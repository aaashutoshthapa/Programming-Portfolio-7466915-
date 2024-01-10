# Modify your "greetings" program so that the first letter of the name entered is
# always in uppercase with the rest in lowercase. This should happen even if the user
# entered their name differently. So if the user entered arthur, ARTHUR, or even
# arTHur the name should be displayed as Arthur.




# Define a function 'greetings' that greets a person by their name
def greetings(name):
    name = name.capitalize()  # Capitalize the first letter of the name
    print(f"Hello, {name}!")  # Display a greeting message with the capitalized name

# Prompt the user to enter their name
name = input("Please enter your name: ")

# Call the 'greetings' function and pass the entered name as an argument
greetings(name)
