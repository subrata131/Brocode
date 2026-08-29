import random

def spin():
    sym=["🍓", "⭐", "🍉", "🍋", "🚗"]
    return [random.choice(sym) for _ in range(3)]
    
def show(row):
    print("=========================")
    print(" | ".join(row))
    print("=========================")
def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍓":
            return bet*3
        elif row[0]=="🍋":
            return bet*4
        elif row[0]=="🍉":
            return bet*5
        elif row[0]=="⭐":
            return bet*10
        elif row[0]=="🚗":
            return bet*20
    return 0  

    
def main():
    balance=100
    print("=========================")
    print("Welcome To Python Slot ")
    print("Symbol:🍓 ⭐ 🍉 🍋 🚗")
    print("=========================")
    while balance>0:
        print("=========================")
        print(f"Current Balnce is:{balance}")
        print("=========================")
        bet=input("Enter Your Bet Ammount:")

        if not bet.isdigit():
            print("Enter valid Input")
            continue
        bet= int(bet)
        if bet>balance:
            print("Inufficient Balance")
            continue
        if bet<0:
            print("Bet Must be Grater Than 0")

        balance-=bet
        row=spin()
        
        print("Spining..\n")
        show(row)
        m=payout(row,bet)
        if m>0:
            print(f"You won{m}")
        else:
            print("Sorry YOu lost")

        balance+=m
        print("=========================")
        n=input("Do you want to play Again?(Y/N)").lower()

        if n!="y":
            break

    print("=========================")
    print(f"Game Over Your Balance:{balance}")



if __name__ =="__main__":
    main()
