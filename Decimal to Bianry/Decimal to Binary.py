n = int(input("Enter A Number: "))
bin = 0
p = 0
while(n>0):
    r = n%2
    bin = bin+10**p*r
    p = p+1
    n = n//2
print(f"Binary Equivalent = {bin}")