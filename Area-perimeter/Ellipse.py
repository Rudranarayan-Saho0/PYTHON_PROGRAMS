import math
def Ellipse(a,b):
    Area = math.pi*a*b
    Perimeter = math.pi*(3*(a+b)-math.sqrt((3*a+b)*(a+3*b)))
    return Area,Perimeter

a = float(input('Enter First Axis: '))
b = float(input('Enter Second Axis: '))

Area, Perimeter = Ellipse(a,b)

print(f'The Area Of The Ellipse is {Area}')
print(f'The Perimeter Of The Ellipse is {Perimeter}')