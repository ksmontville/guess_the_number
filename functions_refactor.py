from random import randint

logo = """
 __        ___  __   __     ___       ___                     __   ___  __    /
/ _` |  | |__  /__` /__`     |  |__| |__     |\ | |  |  |\/| |__) |__  |__)  / 
\__> \__/ |___ .__/ .__/     |  |  | |___    | \| \__/  |  | |__) |___ |  \ .  

"""


def game_intro(art):
    print(art)
    print("Welcome to Guess the Number!")


def select_difficulty():
    """Returns a number of available guesses based on difficulty. 10 for easy, 5 for hard."""
    available_guesses = input("Select a difficulty: easy (10 guesses), hard (5 guesses)\n")

    if available_guesses.lower() == 'easy':
        available_guesses = 10
    elif available_guesses.lower() == 'hard':
        available_guesses = 5
    else:
        print("Invalid selection. Default guesses set to 10.")
        available_guesses = 10

    return available_guesses


def generate_hidden_number():
    """Generate a random number between 1 and 100."""
    print("\nI am thinking of a number between 1 and 100...")
    print("(type 'q' at any time to quit)\n")
    return randint(1, 100)


def make_guess(guesses_remaining):
    print(f"You have {guesses_remaining} guesses remaining.")
    return input("Make a guess: ")


def compare_numbers(guess, answer, turns):
    """Main loop for the game."""
    if int(guess) == answer:
        print(f"You guessed {answer} correctly!\n")
    elif int(guess) > answer:
        print("You guessed too high.\n")
        return turns - 1
    elif int(guess) < answer:
        print("You guessed too low.\n")
        return turns - 1


def check_game_quit(guess):
    if guess.lower() == 'q':
        print("\nThanks for playing!")
        return True
    else:
        pass


def check_game_over(guess, answer, difficulty):
    if difficulty == 0:
        print(f"You are all out of guesses!\n")
        return True
    elif int(guess) == answer:
        return True
    else:
        pass


def check_play_again():
    prompt = input("Play again? y/n ")
    if prompt.lower() == 'y':
        return True
    else:
        print("\nThanks for playing!")
        return False
