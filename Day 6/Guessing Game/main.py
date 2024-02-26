import random

def guessing_game():
    print("Welcome to the guessing game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    secret_number = random.randint(1, 100)

    guess = None
    attempts = 0

    while guess != secret_number:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        guessing_game()
    else:
        print("Thanks for playing!")

guessing_game()
