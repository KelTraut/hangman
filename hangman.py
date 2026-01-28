from random import Random

def get_randomizer(seed: int) -> Random:
    rand = Random(seed)
    return rand

def get_random_secret_word(secrets: list[str], r: Random) -> list[str]:
    """
    Given a list of secret words + a random number generator r,
    returns a random word from that list
    """
    secret = []
    random_index = r.randint(0, len(secrets) - 1)
    selected_secret_word = secrets[random_index]
    for char in selected_secret_word:
        secret.append(char)
    return secret

def get_guess(secret: list[str], found: list[bool]) -> str:
    print(stringify_game_progress(secret, found), end="")
    guess = input("Enter next guess (lowercase letter): ")
    done = False
    while not done:
        if (len(guess) == 1) and (guess.islower()):
            done = True
        else:
            guess = input("Enter next guess (lowercase letter): ")
    return guess

def in_secret_word(guess_letter: str, secret: list[str]) -> bool:
    if guess_letter in secret:
        return True
    else:
        return False

def stringify_game_progress(secret: list[str], found: list[bool]) -> str:
    found_string = ""
    for i in range(0, len(found)):
        if found[i]:
            found_string = found_string + secret[i] + " "
        else:
            found_string = found_string + "_" + " "
    return found_string

def load_dictionary(filename: str) -> list[str]:
    result = []
    with open(filename, "r") as input_file:
        for line in input_file:
            line = line.lower()
            result.append(line.strip())
    return result

def initialize_game_state(secret: list[str]) -> list[bool]:
    found = []
    for i in range(0, len(secret)):
        found.append(False)
    return found

def update_progress(correct_guess: str, secret: list[str], found: list[bool]) -> list[bool]:
    for i in range(0, len(found)):
        if correct_guess == secret[i]:
            found[i] = True
        else:
            found[i] = found[i]
    return found

def guessed_all_letters(found: list[bool]) -> bool:
    done = True
    for i in range(0, len(found)):
        if not found[i]:
            done = False
    return done

def play(secret: list[str]) -> None:
    found = initialize_game_state(secret)
    lives = 8
    done = False
    while lives > 0 and not done:
        guess_letter = get_guess(secret, found)
        if in_secret_word(guess_letter, secret):
            found = update_progress(guess_letter, secret, found)
        else:
            lives = lives - 1
            print(">> You've got", lives, "misses left")
        if guessed_all_letters(found):
            done = True
            secret_string = ""
            for i in range(0, len(secret)):
                secret_string = secret_string + secret[i]
            print("Well done! The secret word was", secret_string)

def main() -> None:
    secret_words = load_dictionary("list.txt")
    print("Loaded Dictionary...")
    r = get_randomizer(101)
    secret = get_random_secret_word(secret_words, r)
    play(secret)\

main()