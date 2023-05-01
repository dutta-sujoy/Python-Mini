from random import randint
logo = """   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          """
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
# function to cheak user guess against actual number


def cheak_answer(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too Low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")

# make function to set dificulty


def set_dificulty():
    level = input("Choose a dificulty. Type 'easy' or 'hard':")
    if level == 'easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN


def game():
    # choseing random number between 1 to 100
    print(logo)
    print("Welcome to My Number Guessing Game :)")
    print("I am thinking of an number between 1 to 100.")
    answer = randint(1, 101)
    turns = set_dificulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    # repet the guessing functiom if it is wrong
    guess = 0
    while guess != answer:
        # let the user guess the number
        guess = int(input("Make a guess:"))
        turns = cheak_answer(guess, answer, turns)
        print(f"You have {turns} attempts remaining to guess the number.")
        if turns == 0:
            print(
                f"You've run out the guesses , You lose!. The answer is {answer}")
            return


game()
