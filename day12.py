import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1, 101)
if user_choice == 'hard':
    attempts = 5
elif user_choice == 'easy':
    attempts = 10
else:
    print("Invalid input. Please restart the game.")
    exit()

def guess_number():
    try:
        return int(input("Make a guess: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return guess_number()
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    user_guess = guess_number()
    if user_guess < number:
        print("Too low.")
    elif user_guess > number:
        print("Too high.")
    else:
        print(f"Congratulations! You guessed the number {number}.")
        break
    attempts -= 1
    if attempts == 0:
        print(f"You've run out of guesses. The number was {number}. Better luck next time!")
