import random

def num_generator():
    return random.randint(1011, 9999)

def get_digits(num):
    return [int(d) for d in str(num)]

def repeated_num_checker(list_num):
    return len(list_num) != len(set(list_num))

def num_bulls_cows(guess1, guess2):
    # cows = [a for a, b in zip(guess1, guess2) if a == b]

    # common = set(guess1) & set(guess2)
    # bulls = [val for val in common if val not in common]

    bulls = 0
    cows = 0

    for i in range(4):
        if guess1[i] == guess2[i]:
            bulls += 1
        elif guess1[i] in guess2:
            cows += 1

    return bulls, cows

def game():
    print('Welcome to the Cows And Bulls Game.')
    tries = int(input("Enter number of tries: "))

    secret = num_generator()
    while repeated_num_checker(get_digits(secret)):
        secret = num_generator()
    comp_guess = get_digits(secret)
    print(comp_guess)

    while tries > 0:
        human_guess = get_digits(input("Type in a 4 digit number guess: "))
        bulls, cows = num_bulls_cows(human_guess, comp_guess)

        print(f"{bulls} bulls, {cows} cows ")
        tries -= 1

        if bulls == 4:
            print('You guessed right.')
            break

    else:
        print('You ran out of tries')


game()