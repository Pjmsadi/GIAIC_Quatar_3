import random

print("Welcome to the Number Guessing Game! \n you got 5 chances to guess the number between 1 to 100")

number_to_guess = random.randrange(5, 50)

chance = 5

guess_counter = 0

while guess_counter < chance:
    guess_counter += 1
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print(f"The number was {number_to_guess} and you guessed it right in {guess_counter} guesses")
        break
    elif guess_counter >= chance and guess != number_to_guess:
        print(f"Sorry you have run out of chances. The number was {number_to_guess}")
    elif guess < number_to_guess:
        print("Too low")
    else:
        print("Too high")