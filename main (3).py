import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        user_guess = input("Take a guess: ")

        # Check if the input is a valid number
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue

        user_guess = int(user_guess)
        attempts += 1

        if user_guess < number_to_guess:
            print("Your guess is too low. Try again!")
        elif user_guess > number_to_guess:
            print("Your guess is too high. Try again!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Call the function to start the game
guess_the_number()
