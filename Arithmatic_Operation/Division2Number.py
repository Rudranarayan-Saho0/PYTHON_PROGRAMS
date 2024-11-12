#Arithmatic Operation - Division Two Numbers..

#User-Input: ask to User For Input two Numbers
Num1 = float(input("Enter First Number: "))
Num2 = float(input("Enter Second Number: "))

#Check The Conditions
if Num2 == 0:
    print("Error: Division By Zero Is Not Allowed")
else:
    print(f" {Num1} / {Num2} = {Num1 / Num2}")  #print The Result