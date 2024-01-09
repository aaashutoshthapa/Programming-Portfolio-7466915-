# A kindly teacher wishes to distribute a tub of sweets between her pupils. She will
# first count the sweets and then divide them according to how many pupils attend
# that day. Write a program that will tell the teacher how many sweets to give to each
# pupil, and how many she will have left over.


total_sweeets=int(input("How many sweets are there?"))     # Prompt the user to enter the total number of sweets available
pupil_count=int(input("how many pupil are present today?"))   # Prompt the user to enter the number of pupils present


# Calculate the number of sweets each pupil will get and any remaining sweets
sweets_per_pupil= total_sweeets // pupil_count
left_over_sweet= total_sweeets%pupil_count

print(f"Each pupil will get {sweets_per_pupil} sweets and {left_over_sweet} are remaning out")