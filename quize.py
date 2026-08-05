questions=("What is the capital city of France? ",
           "Which planet is known as the 'Red Planet'?",
           "What is the chemical symbol for gold?",
           "Who wrote the play 'Romeo and Juliet'?",
           "What is the largest ocean on Earth?",
           "Which element is essential for human respiration?")

options=(("A.London","B.Berlin","C.Paris","D.Madrid"),
         ("A.Venus","B.Mars","C.jupiter","D.Saturn"),
         ("A.Ag","B.Au","C.Fe","D.Pb"),
         ("A.Chaeles Dickens","B.Jane Austen","C.William Shakespeare","D.Mark Twain"),
         ("A.Atlantic Ocean","B.Indian Ocean","C.Arctic Ocean","D.Pacific Ocean"),
         ("A.Oxygen","B.Carbon Dioxide","C.Nitrogen","D.Hydrogen"))

answers=("C","B","B","C","D","A")
guesses = []
score=0
questions_number=0

for i in questions:
    print("----------------------------")
    print(i)
    for j in options[questions_number]:
        print(j)

    guess=input("Enter(A, B, C, or D): ").upper()
    guesses.append(guess)
    if guess==answers[questions_number]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[questions_number]} is the correct answer.")

    questions_number+=1

print("----------------------------")
print("          RESULTS           ")
print("----------------------------")
print("Answers:",end="")
for i in answers:
    print(i,end=" ")
print()

print("Guesses:",end="")
for i in guesses:
    print(i,end=" ")
print()

score = score /len(questions)*100
print(f"Your score is: {score}%")