num = int(input('Enter a Number'))
factorial = 1
for num in range (1,num+1):
    factorial*=num

print(f'The factorial Of a {num} is {factorial}')