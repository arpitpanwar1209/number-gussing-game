import random

def get_random_number(start=1, end=100):
    return random.randint(start, end)

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("Oops! That's not a valid number. Try again.")

def play_game():
    number = get_random_number()
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100. Try to guess it!")

    while True:
        guess = get_user_guess()
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
            break

if __name__ == "__main__":
    play_game()
