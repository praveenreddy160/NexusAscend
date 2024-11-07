import random

def play_hangman():
    words = ["Hyderabad", "Boduppal", "Tarnaka", "Uppal"]
    picked_word = random.choice(words)
    display_word = ["_"] * len(picked_word)
    lives = 6

    while lives > 0 and "_" in display_word:
        print(" ".join(display_word))
        print(f"Total_Lives remaining: {lives}")
        guess = input("Guess a letter: ").lower()

        if guess in picked_word:
            for i in range(len(picked_word)):   # this will get kicked in when the guess is in picked word and starts comparing with i numbers and whatever the number has the same letter that will be taken in display and picked word
                # print(i)
                if picked_word[i] == guess:
                    display_word[i] = guess
                    print(f"picked_word[{i}]: {picked_word[i]}, display_word[{i}]: {display_word[i]}") 
        else:
            lives -= 1
            print("Incorrect guess.")

    if "_" not in display_word:
        print(" ".join(display_word))
        print("You won!")
    else:
        print(f"You lost! The word was {picked_word}")

play_hangman()

