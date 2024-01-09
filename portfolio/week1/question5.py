# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group.

student_counts = [113, 175, 12]  # list of student 


for student_count in student_counts:  # Loop through each student count in the list
    full_groups = student_count // 24    # Calculate the number of full groups of 24 students
    left_over_students = student_count % 24   # Calculate the number of students left after forming full groups
    print(f"For {student_count} students, there will be {full_groups} full groups and {left_over_students} students in the smaller 'left over' group.")