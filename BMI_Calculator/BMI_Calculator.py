# A Python Program To Calculate The BMI Of a Person.
height = float(input("Enter Your Height In Meters. "))
weight = float(input("Enter Your Weight In K.G. "))

BMI = weight/(height**2)

print(f"Your BMI Is {BMI: .2f}")

#Catagorize Based on Their Weight & Height.
if BMI<18.5:
    print("Under weight.")
elif 18.5<=BMI<24.9:
    print("Normal Weight.")
elif 25<=BMI<29.9:
    print("Over Weight")
else:
    print("Obese")