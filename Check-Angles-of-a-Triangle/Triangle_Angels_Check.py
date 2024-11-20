#Check The Entered angle is Acute, Obtuse or Right Angle.

Angle = float(input("Enter Angle In degrees: "))

if 0<Angle<90:
    print("The Angle Is Acute. ")
elif Angle ==90:
    print("The Angle Is Right Angle. ")
elif 90<Angle<180:
    print("The Angle Is Obtuse. ")
else:
    print("Invalid Angle")