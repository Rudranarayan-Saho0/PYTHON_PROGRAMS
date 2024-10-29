from datetime import datetime

def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Input: birthdate in YYYY-MM-DD format
birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
age = calculate_age(birthdate)
print(f"You are {age} years old.")
