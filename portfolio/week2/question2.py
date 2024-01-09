# Write a program that prompts a user to enter a temperature in Celsius, and then
# displays the corresponding temperature in Fahrenheit, like so:
# Enter a temperature in Celsius: 32.5
# 32.5C is equivalent to 90.5F.


temp=float(input("Enter a temperature in Celsius: "))  # Prompt the user to enter a temperature in Celsius and convert it to a floating-point number
Fahrenheit=temp*9/5+32  # Converting temp to fahrenheit
print(f"{temp}C is equivelent to {Fahrenheit}F")  

