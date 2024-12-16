#Check the Number Is Prime Or Composite Using While Loop..
n = int(input('Enter a Number: '))
i =2
while (i<= n//2):
    if n%i == 0:
        print("Composite")
        break
    i =i+1
if i>n/2:
    print("prime")