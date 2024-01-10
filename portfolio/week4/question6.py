# Write a program that takes a centigrade temperature and displays the equivalent in
# fahrenheit. The input should be a number followed by a letter C. The output should
# be in the same format

def get_input():
    # Prompt the user to enter a temperature in Celsius and return the input
    temp = (input("Enter Temperature which is centrigrate and have its initial i.e. C: "))
    return temp

def calc(temp):

    if temp.endswith(('C', 'c')):  # Checks if the input ends with 'C' or 'c'
        try:
            celsius = float(temp[:-1])  # Extracts the numerical part and converts it to float
            fahrenheit = celsius * 9 / 5 + 32  # Converts Celsius to Fahrenheit
            return fahrenheit  # Returns the temperature in Fahrenheit
        except ValueError:
            return "Invalid input. Please enter a valid temperature in the format 'numberC'."
            # Returns an error message for invalid input format
    else:
        return "Invalid format. Please enter the temperature followed by 'C' or 'c'."
        # Returns an error message for an invalid temperature format

        
def display(temp,f):
    print(f"{temp} is equivalent to {f}F")
     # Display the equivalent temperature in Fahrenheit
    
temp=get_input()
# Get the temperature input from the user

f=calc(temp)
# Convert the temperature from Celsius to Fahrenheit using the calc function

display(temp,f)
# Display the original temperature in Celsius and the converted temperature in Fahrenheit




