#This Program is used to guess a randomly generated number by the computer
import random
random = random.randint(1, 100)
while True:
    guess_number = int(input("Enter A Number : "))
    if guess_number >= 70:
        print("Your Number Is Too High")
    elif guess_number <= 40:
        print("Your Number Is Too Low")
    else:
        print("You Made The Right Guess")