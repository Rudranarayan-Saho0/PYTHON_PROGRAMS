
def Trapezoid(a,b,c,d,heightr):
    Area = 0.5*(a+b)*height
    Perimeter = a+b+c+d
    return Area,Perimeter

a = float(input('Enter 1st Side Lenght: '))
b = float(input('Enter 2nd Side Length: '))
c = float(input('Enter 3rd side Length: '))
d = float(input('Enter 4th side Length: '))
height = float(input('Enter Height OF The Trapezium: '))

Area,Perimeter = Trapezoid(a,b,c,d,height)
print(f'Area Of The Trapezoid Is {Area}')
print(f'Perimeter Of The Trapezoid Is {Perimeter}')