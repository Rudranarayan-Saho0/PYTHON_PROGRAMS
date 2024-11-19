num1 = int(input('Enter a Number'))
num2 = int(input('enter second Number'))
num3 = int(input('nter Third Number'))

Greater = num1 if num1>num2 and num1>num3 else num2 if num2>num3 else num3
print(f"The Greatest Number is = {Greater}")