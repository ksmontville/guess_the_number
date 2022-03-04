from random import randint

from functions import logo, decrease_guesses


print(logo)

difficulty = input("Select a difficulty: easy (10 guesses), hard (5 guesses)\n")

if difficulty.lower() == 'easy':
    AVAILABLE_GUESSES = 10
elif difficulty.lower() == 'hard':
    AVAILABLE_GUESSES = 5
else:
    print("Invalid selection. Default guesses set to 10.")
    AVAILABLE_GUESSES = 10


playing = True
while playing:
    print("Type 'q' at any time to quit.\n")
    print("I am thinking of a number between 1 and 100...")
    hidden_number = randint(1, 100)

    remaining_guesses = AVAILABLE_GUESSES

    while remaining_guesses > 0:
        player_guess = input("Your guess: ")

        if player_guess.lower() == 'q':
            print("\nThanks for playing!")
            playing = False
            break
        elif int(player_guess) == hidden_number:
            print(f"You guessed {hidden_number} correctly!")
            break
        elif int(player_guess) > hidden_number:
            print("You guessed too high.")
            remaining_guesses = decrease_guesses(remaining_guesses)
        elif int(player_guess) < hidden_number:
            print("You guessed too low.")
            remaining_guesses = decrease_guesses(remaining_guesses)

        if remaining_guesses == 0:
            print(f"I was thinking of the number {hidden_number}!\n")

    if playing:
        play_again = input("\nPlay again? y/n ")
        if play_again == 'y':
            continue
        else:
            print("\nThanks for playing!")
            break
