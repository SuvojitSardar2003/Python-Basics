# 2. WAP to accept marks of 6 students and display them in a sorted manner.

marks = []
for i in range(6):
    mark = float(input("Enter the marks of student: "))
    marks.append(mark)
marks.sort()
print("The sorted marks of the students are:")
print(marks)