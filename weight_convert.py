weight=float(input("Enter your weight:"))
unit=input("Enter the unit of weight kilograms or pounds (K or L):")

if unit=="K":
    weight=weight*2.205
    unit="pounds"
elif unit=="L":
    weight=weight/2.205
    unit="kilograms"
else:
    print("Invalid unit")

print(f"Your weight is:{round(weight,1)} {unit}")