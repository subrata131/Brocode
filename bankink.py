
def show(balance):
    print("=========================")
    print("Your Account Balance is:",balance)
    print("=========================")
   

def deposite():
    print("=========================")
    m=int(input("Enter Amount To deposite:"))
    if m<0:
        print("=========================")
        print("Invalid ammount")
        return 0
    else:
        print("=========================")
        print("Deposite Scuccessful!!")
        return m
        
   
def withdraw(balance):
    print("=========================")
    m=int(input("Enter Amount To Withdraw:"))
    if m>balance:
        print("=========================")
        print("Insufficient Balance")
        return 0
    else:
        print("=========================")
        print("Withdraw Scuccessful!!")
        return m

def main():
    balance=0
    while True:
        print("===Banking Program===")
        print("1. Show Balance\n2. Deposite\n3. Withdraw\n4. Exit")

        n=int(input("Enter Your Choice:"))
        if n==1:
            show(balance)
        elif n==2:
            balance+=deposite()
        elif n==3:
            balance-=withdraw(balance)
        elif n==4:
            break
        else:
            print("Invalid Input")

if __name__=="__main__":
    main()
            
        
