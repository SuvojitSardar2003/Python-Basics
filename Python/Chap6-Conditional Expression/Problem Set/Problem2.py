# 2. WAP to find out whether a student has passes or failed if it requires a total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

marks1 = int(input("Enter marks of subject 1: "))
marks2 = int(input("Enter marks of subject 2: "))
marks3 = int(input("Enter marks of subject 3: "))

# Calculate total marks and percentage
total_percentage = (marks1 + marks2 + marks3 ) / 3

if(total_percentage >= 40 and marks1 >=33 and marks2 >=33 and marks3 >= 33):
    print("Congratulations! You have passed.")
else:
    print("Sorry! You have failed.")