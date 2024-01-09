# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).


matches=609
batted=1014
wasnt_out=162
scored=48426
# aAssigning the values of matches, batted, wasnt_out, scored

completed_innings = batted - wasnt_out  #calculating completed innings
batting_average = scored / completed_innings  #calculating batting average 
print(f"In long career of Yorkshire, Geoffrey Boycott the batting average is: {batting_average}")
