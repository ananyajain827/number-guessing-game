
import random
guesses=0
is_running=True
lowest_num=1
highest_num=100
answer=random.randint(lowest_num,highest_num)

while is_running:
    guess=input("please enter any guess between 1 to 100\n")

    if guess.isdigit():
        guess=int(guess)
        guesses+=1
        if guess<lowest_num or guess>highest_num:
            print("That number is out of range.please enter any guess between 1 to 100\n")
        elif guess<answer:
            print("Too Low.Try again\n")
        elif guess>answer:
            print("Too High.Try again\n")
        else:
            print("congratulations!!!!!your guess is correct :)\n")
            print(f"number of guesses are {guesses}")
            is_running=False
    else:
        print("invalid guess")