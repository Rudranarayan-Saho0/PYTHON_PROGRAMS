import math
def Circle(radius):
    Area = math.pi*radius*radius
    Circumference = 2*math.pi*radius
    return Area, Circumference

radius = float(input('Enter The Radius Of The Circle: '))

Area,Circumference = Circle(radius)
print(f'The Area Of The Circle Is {Area}')
print(f'The Circumference Of The Circle is {Circumference}')