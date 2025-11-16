import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the lower bound of the range: "))
high = int(input("Enter the upper bound of the range: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")


num = random.randint(low, high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int (input("Enter your guess: "))

    if guess == num:
        print(f"Congratulations! You've guessed the number {num} correctly in {gc} attempts.")
        break
    elif gc >= ch and guess != num:
        print(f"Sorry, The number was {num}. Better luck next time!")

    elif guess < num:
        print("Your guess is too low. ")

    elif guess > num:
        print("Your guess is too high")

