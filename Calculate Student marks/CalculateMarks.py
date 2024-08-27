name = input("Enter your name: ")

marks1 = float(input("Enter marks for subject 1: "))
marks2 = float(input("Enter marks for subject 2: "))
marks3 = float(input("Enter marks for subject 3: "))
marks4 = float(input("Enter marks for subject 4: "))
marks5 = float(input("Enter marks for subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = total_marks / 5

if percentage > 90:
    grade = 'O'
elif percentage > 80:
    grade = 'E'
elif percentage > 70:
    grade = 'A'
elif percentage > 60:
    grade = 'B'
else:
    grade = 'Fail'

print(f"\nName: {name}\nPercentage: {percentage:.2f}%\nGrade: {grade}")
