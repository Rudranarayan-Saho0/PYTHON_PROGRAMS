#Program To Accept A Number And Print The Corresponding Days Of The Week.
days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
num = int(input('Enter a Number between 1 to 7: '))
if 1<=num<=7:
    print({days[num-1]})
else:
    print('Invalid Number')