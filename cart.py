foods=[]
prices=[]
total=0

while True:
    food=input("Enter the item to buy (q to quit or Exit):")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of {food}:"))
        foods.append(food)
        prices.append(price)


print("===== YOUR CART =====")
for i in foods:
    print(i,end=" ")

for i in prices:
    total+=i

print(f"\nYour Total Cart price is: {total}")
