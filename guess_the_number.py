from random import randint

easy_level_turns = 10
hard_level_turns = 5

def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if user_guess > actual_answer:
        print("Too High")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You Guessed it right! the actual answer is {actual_answer}")

def set_difficulty():
    level = input("Please enter your difficulty Level, 'easy' or 'hard':\n")
    if level.lower() == "easy":
        return easy_level_turns
    else:
        return hard_level_turns
        
def game():
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("i'm thinking of a number between 1-100, what do you say???")
    actual_answer = randint(1, 100)
    
    turns = set_difficulty()
    print(f"you have {turns} attempts remaining to guess the number.")

    user_guess = 0
    while user_guess != actual_answer:
        user_guess = int(input("Make a Guess: \n"))
        turns = check_answer(user_guess, actual_answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user_guess != actual_answer:
            print(f"You have {turns} attempts remaining to guess the number.")

game()