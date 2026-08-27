menu={
    "pizza": 100.00,
    "burger": 99.00,
    "poporn": 110.00,
    "fries": 80.00
}
total=0
cart=[]
print("----------Items------------")
for key,values in menu.items():
    print(f"{key:10}= {values:.2f}")
print("---------------------------")

while True:
    n=input("Enter item to buy (q for quit): ").lower()
    if n=="q":
        break
    elif menu.get(n) is not None:
        cart.append(n)

print("-----------Your Cart------------")
for i in cart:
    total+=menu.get(i)
    print(i, end=" ")

print(f"\nTotal is: {total:.2f}")
