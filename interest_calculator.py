principle= 0
rate = 0
time = 0

while principle <= 0:
    principle=float(input("Enter the priniciple amount:"))
    if principle <=0:
        print("Principle can not be less than or equal to zero.")

while rate <=0:
    rate=float(input("Enter the rate of interest:"))
    if rate <=0:
        print("Interest rate can not be less than or equal to zero")


while time <=0:
    time=int(input("Enter the time period in years:"))
    if time <=0:
        print("Time period can not be less than or equal to zero")

total=principle * pow((1+rate/100),time)
print(f"Balace after {time} years is: {total:.2f}")



