import random

def guess(x):
    random_number = random.randint(1, x)
    
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess > random_number:
            print("Too High, Guess again")
        else:
            print("Too Low, Guess again")
    
    print(f"YAY, congrats. You've guessed the number {guess} correctly")

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
            

        feedback = input(f"Is {guess} too high (h), too low (l) or correct (c)??").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    
    print(f"Yay! the computer guessed {guess} correctly")


computer_guess(100)