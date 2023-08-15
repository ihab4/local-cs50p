import random
import sys

def main():
    level = getlevel()
    number = random.randint(1,level)
    while True:
        guess = getguess(level)
        if check(guess, number) == True:
            sys.exit("Just right!")


def getlevel():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 100:
                return level
        except ValueError:
            pass

def getguess(level):
    while True:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= level:
                return guess
        except ValueError:
            pass
    
def check(guess, number):
    if guess == number:
        return True
    if guess > number:
        print("Too large!")
    else:
        print("Too small!")

    return False
    



main()