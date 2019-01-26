import random
from random import randint
gen = random.randint(1,6)
def main():
    global gen
    #print(gen)
    guess = int(input("Enter guess: "))
    if guess == gen:
        print("you guessed right!")
    if guess > gen:
        print("too high")
        main()
    if guess < gen:
        print("too low")
        main()
main()
