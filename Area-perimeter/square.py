def Square(side):
    Area = side*side
    Perimeter = 4*side
    return Area, Perimeter

side = float(input("Enter The Length Of The Square: "))

Area,Perimeter = Square(side)

print(f'The Area Of The Square is {Area}')
print(f'The Perimeter Of The Square Is {Perimeter}')
