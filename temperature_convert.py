unit=input("Is this Temperature in Celsius or Fahrenheit(C or F):")
temp=float(input("Enter the Temperature:"))

if unit=="C":
    temp=(temp*9/5)+32
    unit="Fahrenheit"
elif unit=="F":
    temp=(temp-32)*5/9
    unit="Celsius"
else:
    print(f"{unit} is not valid unit")

print(f"The Temperature is:{round(temp,1)} {unit}")