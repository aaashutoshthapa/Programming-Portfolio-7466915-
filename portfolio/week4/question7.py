# Write a program that reads 6 temperatures (in the same format as before), and
# displays the maximum, minimum, and mean of the values.
# Hint: You should know there are built-in functions for max and min. If you hunt, you
# might also find one for the mean
def get_temp():
    temp=[]   # Create an empty list to store temperature values
    for i in range(6):   # Iterate six times to collect temperature values
        
        x=float(input(f"Enter {i+1}th tempature in celcious: "))  # Prompt the user to enter a temperature in Celsius and append it to the list
        
        temp.append(x)  # Append the entered temperature to the 'temp' list
    return temp
    
def calc(temp):
    max_temp = max(temp)  # Find the maximum temperature in the 'temp' list
    min_temp = min(temp)  # Find the minimum temperature in the 'temp' list
    sum_temp = sum(temp)  # Calculate the sum of all temperature values in the 'temp' list
    avg_temp = sum_temp / len(temp)  # Calculate the average temperature from the 'temp' list
    return max_temp,min_temp,avg_temp

def display():
    print(f"The maxmium temp of {temp} is: {max_temp}")
    print(f"The minium temp of {temp} is: {min_temp}")
    print(f"The average temp of {temp} is: {avg_temp:.2f}")

temp=get_temp()
# Get the temperature values from the user using the get_temp() function

max_temp,min_temp,avg_temp=calc(temp)
# Calculate the maximum, minimum, and average temperatures using the calc() function

display()
