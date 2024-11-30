n = int(input("Enter Number Of Terms: "))
a,b = 0,1
count =2
print(a)
while (count<=n):
    c = a+b
    print(c)
    a=b
    b=c
    count+=1
