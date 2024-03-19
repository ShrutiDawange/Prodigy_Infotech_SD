import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right! The number was {number_to_guess}.")
            print(f"It took you {attempts} attempts to win the game.")
            break

if __name__ == "__main__":
    guessing_game()
