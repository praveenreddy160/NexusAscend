import random

def rock_paper_scissors():
    # created a Dictionary to store choices and ASCII art
    choices = {
        "scissors": '''  
            _       ,/'
           (_)   ,/'
             _   ::
           (_) '   `\.
               `\.
        ''',
        "rock": '''                       
           888      
           888      
           888      
    888d888 .d88b.  .d8888b888  888 
    888P"  d88""88bd88P"   888 .88P 
    888    888  888888     888888K  
    888    Y88..88PY88b.   888 "88b 
    888     "Y88P"  "Y8888P888  888 
        ''',
        "paper": ''' 
       _ __   __ _ _ __   ___ _ __ 
      | '_ \ / _` | '_ \ / _ \ '__|
      | |_) | (_| | |_) |  __/ |   
      | .__/ \__,_| .__/ \___|_|   
      | |         | |              
      |_|         |_|              
        '''
    }

    # Randomly selecting a choice for the computer
    pc_choice = random.choice(list(choices.keys()))

    # Taking the user's choice
    user_choice = input("Choose rock, paper or scissors: ").lower()

    # Validating the user's choice
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    print(f"\nComputer chose:\n{choices[pc_choice]}")
    print(f"\nYou chose:\n{choices[user_choice]}")

    # Determine the outcome
    if user_choice == pc_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and pc_choice == "scissors") or \
         (user_choice == "scissors" and pc_choice == "paper") or \
         (user_choice == "paper" and pc_choice == "rock"):
        print("You win!")
    else:
        print("You lose!")

# Run the game
rock_paper_scissors()
