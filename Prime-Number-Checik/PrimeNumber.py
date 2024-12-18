def is_Prime(n):
#Check The Number Is Prime
    if n<=1:
        return False
    for i in range (2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
#Test The Function
number = 30
if is_Prime(number):
    print(f"{number} is a prime Number")
else:
    print(f"{number} is not a prime Number")