import random

option=("rock","paper","scissors")
player=None
com=random.choice(option)

while player not in option:
    player=input("Enter a choice (rock, paper, scissors): ").lower()

print(f"Player: {player}")
print(f"Computer: {com}")

if player==com:
    print("Its a tie!")
elif player=="rock" and com=="scissors":
    print("You win!")
elif player=="paper" and com=="rock":
    print("You win!")
elif player=="scissors" and com=="paper":
    print("You win!")
else:
    print("You lose!")
