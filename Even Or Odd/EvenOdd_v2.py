def check(number):
    if number%2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"


number = int(input('Enter a Number'))
result = check(number)
print(result)
