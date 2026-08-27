import random
guess=0

answer=random.randint(1,100)

while True:
    g=input("Guess a number:")

    if g.isdigit():
        g=int(g)
        guess+=1

        if g<1 or g>100:
            print("Please guess a number between 1 and 100")
        elif g<answer:
            print("Your guess is too low")
        elif g>answer:
            print("Your guess is too high")
        else:
            print(f"Congratulations! You guessed the number {answer} in {guess} tries.")
            break
    else:
        print("Please enter a valid number.")
        