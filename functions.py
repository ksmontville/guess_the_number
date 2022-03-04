logo = """
 __        ___  __   __     ___       ___                     __   ___  __    /
/ _` |  | |__  /__` /__`     |  |__| |__     |\ | |  |  |\/| |__) |__  |__)  / 
\__> \__/ |___ .__/ .__/     |  |  | |___    | \| \__/  |  | |__) |___ |  \ .  

"""


def decrease_guesses(guesses):
    """Reduce the player's remaining guesses by 1, then print remaining guesses.|"""
    print(f"You have {guesses - 1} guesses remaining.\n")
    return guesses - 1



