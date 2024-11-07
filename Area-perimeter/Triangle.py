def Triangle(a,b,c,Height):
    Area = 0.5 *b*Height
    Perimeter = a+b+c
    return Area,Perimeter

a = float(input('Enter 1st Side Lenght: '))
b = float(input('Enter 2nd Side Length: '))
c = float(input('Enter 3rd side Length: '))
height = float(input('Enter Height OF The Triangle: '))

Area,Perimeter = Triangle(a,b,c,height)

print(f'The Area Of The Triangle Is {Area}')
print(f'The Perimeter Of The Triangle is {Perimeter}')