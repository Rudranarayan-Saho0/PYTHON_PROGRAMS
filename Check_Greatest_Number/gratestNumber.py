num1 = int(input('Enter a Number'))
num2 = int(input('enter second Number'))
num3 = int(input('nter Third Number'))

if num1>num2:
    if num1>num3:
        greater = num1
    else:
        greater = num3
else:
    if num2>num3:
        greater = num2
    else:
        greater = num3
print(f'The Greatest Number = {greater}')