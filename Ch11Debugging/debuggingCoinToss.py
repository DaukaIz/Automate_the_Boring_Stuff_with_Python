#! python3
# debuggingCoinToss.py: The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game).

import random


def tailHead(guess):
    if guess == "tails":
        return 0
    elif guess == "heads":
        return 1


guess = ""
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == tailHead(guess):
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    if toss == tailHead(guess):
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")
