import random

def pick_credit_cards():
    Bill = ["sunny", "Aaron", "Satti", "PR"]
    return (random.choice(Bill))

new_bill = pick_credit_cards()
print(new_bill)


# def my_fruits():
#     fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
#     vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#     # list of lists: nested lists
    
#     dirty_dozen = [fruits, vegetables]
#     # here we are accessing the 1st list which is vegetables and in that 1st value
    
#     print(dirty_dozen[1][1])
# my_fruits()


# def function(text):
#     return text + text

# def function_2(text):
#     return text.title()

# output = function_2(function("hello"))
# print(output)


# def add(n1, n2):
#     return n1 + n2
# my_favourite_operation = add
# print(my_favourite_operation(2, 3))