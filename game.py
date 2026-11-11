#welcome to guess_lucky_number game

import random

def play_game():
    lucky_number=random.randint(1,50)

    while True:
        guess_number=int(input("enter the number:"))
        if guess_number==lucky_number:
            print("you have got the lucky number, game over \n"
                  "thank you")
            break

        elif guess_number < lucky_number:
            print("your guess is too low")
        else:
            print("your guess is too high")

play_game()