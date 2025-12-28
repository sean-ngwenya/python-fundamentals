from random import randint


# Function to select a random range for the guessing game
def range_guess():
    ranges = [(1, 10), (1, 50), (1, 100), (50, 75), (500, 1000)]
    return ranges[randint(0, len(ranges) - 1)]


# Main function for the number guessing game
def number_guessing_game():
    min_val, max_val = range_guess()
    number_to_guess = randint(min_val, max_val)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between {min_val} and {max_val}.")

    # Allow the user up to 3 attempts to guess the number
    while True:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(
                    f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts."
                )
                break
        except ValueError:
            print("Please enter a valid integer.")

        if attempts >= 3:
            print(
                f"Sorry, you've used all your attempts. The number was {number_to_guess}."
            )
            break

        print(f"You have {3 - attempts} attempts left.")


if __name__ == "__main__":
    number_guessing_game()
