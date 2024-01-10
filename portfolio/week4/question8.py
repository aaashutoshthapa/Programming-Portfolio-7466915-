# Modify the previous program so that it can process any number of values. The input
# terminates when the user just pressed "Enter" at the prompt rather than entering a
# value

def get_temp():
    temp=[]   # Create an empty list to store temperature values
    i=1       # Initialize a counter for the temperature index
    
    
    while True:
        # Continue collecting temperature values until the user enters an empty value
         x=(input(f"Enter {i}th tempature in celcious (press ENTER to stop!!!!!!): ")) # Prompt the user for input
         if x == "":  # If the input is empty, exit the loop
             break
         else:
             temp.append(float(x)) # Convert the entered value to a float and add it to the 'temp' list
             i+=1 # Increment the counter for the next temperature index
    return temp
    
def calc(temp):
    # Calculate the maximum temperature from the list of temperatures
    max_temp = max(temp)

    # Calculate the minimum temperature from the list of temperatures
    min_temp = min(temp)

    # Calculate the sum of all temperatures from the list
    sum_temp = sum(temp)

    # Calculate the average temperature by dividing the sum of temperatures by the number of temperatures
    avg_temp = sum_temp / len(temp)

    return max_temp,min_temp,avg_temp

def display():
    print(f"The maxmium temp of {temp} is: {max_temp}")
    print(f"The minium temp of {temp} is: {min_temp}")
    print(f"The average temp of {temp} is: {avg_temp:.2f}")

temp=get_temp()
max_temp,min_temp,avg_temp=calc(temp)
display()


