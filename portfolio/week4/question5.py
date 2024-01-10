# Write and test a function that converts a temperature measured in degrees
# centigrade into the equivalent in fahrenheit, and another that does the reverse
# conversion. Test both functions. (Google will find you the formulae).

def values(): 
    # Define a function named 'values' that prompts the user for temperature values
    
    first_value=float(input("enter value in centigrade:"))   
    # Prompt the user to enter a temperature value in centigrade and store it as a float
    
    second_value=float(input("Enter value in fahrenheit: ")) 
    # Prompt the user to enter a temperature value in Fahrenheit and store it as a float
    
    return first_value,second_value   
    # Return the entered temperature values as a tuple containing centigrade and Fahrenheit values

def c_to_f(c):
    fahreneit=c*(9/5)+32
    # Convert Celsius to Fahrenheit using the conversion formula
    
    return fahreneit
    # Return the temperature in Fahrenheit

def f_to_c(f):
    c = (f - 32) * (5 / 9)
    # Convert Fahrenheit to Celsius using the conversion formula
    
    return c
    # Return the temperature in Celsius

def display(a, b):
    print("The temperature in centigrade is:", a)
    print("The temperature in Fahrenheit is:", b)

    
    
#function call and the main operation of function   
centigrade,fahreneit=values()
a=c_to_f(centigrade)
b=f_to_c(fahreneit)
display(a,b)
