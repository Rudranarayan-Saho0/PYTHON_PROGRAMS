#Print the HCF Of Two Inputed integers.... 
num1 = int(input("Enter Number : "))
num2 = int(input("Enter Number : "))

if num1 < num2:
    num1, num2 = num2, num1

while num2:
    num1, num2 = num2, num1 % num2

hcf = num1
print(f"HCF of the inputted numbers is {hcf}")

