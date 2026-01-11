'''
Write a program to accept marks of 6 students and display them in a sorted 
manner.
'''
marks = []
s1 = int(input("Enter the marks of first student: "))
marks.append(s1)
s2 = int(input("Enter the marks of second student: "))
marks.append(s2)
s3 = int(input("Enter the marks of second student: "))
marks.append(s3)
s4 = int(input("Enter the marks of second student: "))
marks.append(s4)
s5 = int(input("Enter the marks of second student: "))
marks.append(s5)
s6 = int(input("Enter the marks of second student: "))
marks.append(s6)
marks.sort()
print(marks)
'''
output
Enter the marks of first student: 56
Enter the marks of second student: 98
Enter the marks of second student: 76
Enter the marks of second student: 56
Enter the marks of second student: 34
Enter the marks of second student: 7
[7, 34, 56, 56, 76, 98]

'''