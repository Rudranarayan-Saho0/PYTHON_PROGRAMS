#Check Student Grade Using Dictionary.
name = input("Enter Students Name: ")
student_class = input("Enter Student Class: ")
section = input("Enter Students Section: ")
grade = input("Enter Student Grade (A/B/C/D/E/F): ").upper()

grade_dict = {
    'A': 'OUTSTANDING',
    "B": 'EXCELLENT',
    "C": 'VERY GOOD',
    "D": 'GOOD',
    "E": 'SATISFACTORY',
    "F": 'FAIL'
}

grade_description = grade_dict.get(grade,'Unrecognised')

print(f"\nStudent Name: {name}\nClass: {student_class}\nSection: {section}\nGrade: {grade_description}")