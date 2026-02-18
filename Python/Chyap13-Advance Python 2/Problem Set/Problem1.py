# 1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one

# 2. Wap to input name, marks and phone number of a student and format it using format function like below:

# "The name of the student is Suvo, his marks are 72 and phone number is 9163175484"

name = input("Enter student's name: ")
marks = int(input("Enter student's marks: "))
phone_number = int(input("Enter students's ph. number: "))

string = "The name of the student is {}, his marks are {} and phone number is {}".format(name,marks,phone_number)

print(string)