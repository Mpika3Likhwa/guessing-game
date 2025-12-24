import random


def play_game():
    secret_number = random.randint(1, 10)
    attempts = 0
    guessed = False

    print("I am thinking of a number between 1 and 10.")

    while not guessed:
        user_input = input("Please guess a number between 1 and 10: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("That's not a valid number. Please try again.")
            continue    # Jump to the next iteration

        #Else Evaluate the guess
        attempts += 1

        if guess < secret_number:
            print("Higher!")  # Telling the user to go up
        elif guess > secret_number:
            print("Lower!")  # Telling the user to go down
        else:
            print(f"Correct in {attempts} tries!")
            guessed = True
play_game()