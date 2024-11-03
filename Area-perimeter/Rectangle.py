def Rectangle(length, width):
    area = length*width
    perimeter = 2*(length+width)
    return area, perimeter

length = int(input('Enter Length of The Rectangle: '))
width = int(input('Enter Width Of The Rectangle: '))

area,perimeter = Rectangle(length,width)

print(f'The Area Of The Rectangle is {area} ')
print(f'The Perimeter Of The Rectangle is {perimeter}')