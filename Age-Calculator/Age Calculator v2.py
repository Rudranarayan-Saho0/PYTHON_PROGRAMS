from datetime import datetime

def calculate_age(birthdate):

    try:
        today = datetime.today()
        birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Input: birthdate in YYYY-MM-DD format
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate)

if isinstance(age, int):
    print(f"You are {age} years old.")
else:
    print(age)
