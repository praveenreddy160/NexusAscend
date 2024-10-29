import random

def pick_credit_cards():
    Bill = ["sunny", "Aaron", "Satti", "PR"]
    print(random.choice(Bill))

pick_credit_cards()

def my_fruits():
    fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
    vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
    # list of lists: nested lists
    
    dirty_dozen = [fruits, vegetables]
    # here we are accessing the 1st list which is vegetables and in that 1st value
    
    print(dirty_dozen[1][1])
my_fruits()