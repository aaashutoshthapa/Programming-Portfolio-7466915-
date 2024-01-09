# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is usually 24 students, but this is
# sometimes varied to create groups of similar size. Write a program that prompts for
# the number of students and group size, and then displays how many groups will be
# needed and how many will be left over in a smaller group.
# How many students? 113
# Required group size? 22
# There will be 5 groups with 3 students left over.
# For bonus credit, see if you can fix the grammar in the output. So if there were 101
# students in groups of 20 the output would be:
# There will be 5 groups with 1 student left over.

student_count = int(input("How many students? "))  # Prompts user to enter student number

group_size = int(input("Required group size? "))   # prompts user to enter no of student in a group

# Calculate the number of full groups and any remaining students
full_groups = student_count // group_size
left_over_students = student_count % group_size

print(f"There will be {full_groups} groups with {left_over_students} student{'s' if left_over_students != 1 else ''} left over.")