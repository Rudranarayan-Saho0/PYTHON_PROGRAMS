#A Simple Python Program to Print The Days Of The Month.
month = input("Enter A Month Nmae: ").lower()

day_Month = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31,
}

days = day_Month.get(month,"Invalid Month Name.")
print(f"Number of Days in {month.capitalize()} is : {days}")