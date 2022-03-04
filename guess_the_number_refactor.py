import functions_refactor as f

f.game_intro(f.logo)

playing = True
while playing:
    difficulty = f.select_difficulty()
    answer = f.generate_hidden_number()

    while difficulty != 0:
        guess = f.make_guess(difficulty)
        if f.check_game_quit(guess):
            playing = False
            break
        difficulty = f.compare_numbers(guess, answer, difficulty)

        if f.check_game_over(guess, answer, difficulty):
            if f.check_play_again():
                break
            else:
                playing = False
                break



