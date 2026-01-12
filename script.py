import random


def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret = random.randint(1, 100)
    attempts = 0

    while True:
        guess_text = input("Enter your guess (or type 'q' to quit): ").strip().lower()

        if guess_text == "q":
            print(f"Goodbye! The number was {secret}.")
            break

        if not guess_text.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_text)
        attempts += 1

        if guess < secret:
            print("Too low 👇")
        elif guess > secret:
            print("Too high 👆")
        else:
            print(f"✅ Correct! You guessed it in {attempts} tries.")
            break


if __name__ == "__main__":
    number_guessing_game()
