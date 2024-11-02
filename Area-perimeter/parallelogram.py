def Parallelogram(base,height,side):
    Area = base*height
    Perimeter = 2*(base+side)
    return Area,Perimeter

base = float(input('Enter The Base Of The Parallelogram'))
height = float(input('Enter The Height Of The Parallelogram'))
side = float(input('Enter The Side Of The Parallelogram'))

Area,Perimeter = Parallelogram(base,height,side)
print(f'Area Of The Parallelogram Is {Area}')
print(f'Perimeter Of The Parallelogram Is {Perimeter}')