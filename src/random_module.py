# import random

# def pick_credit_cards():
#     Bill = ["sunny", "Aaron", "Satti", "PR"]
#     return (random.choice(Bill))

# new_bill = pick_credit_cards()
# print(new_bill)


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


with open("C:/Users/prave/NexusAscend/note.txt", "w+") as file:
    num_chars_written = file.write("I Love You Neha")
    file.seek(0)
    print(num_chars_written)
    print(file.read())
""""Successful"""


# place_holder = "[name]"
# with open("./Input/Names/invited_names.txt") as file:
#     Letter = file.readlines()

# with open("./Input/Letters/starting_letter.txt") as file:
#     letter1 = file.read()
#     # print(letter1)
#     for name in Letter:
#         stripped_name = name.strip()
#         new_letter = letter1.replace(place_holder, stripped_name)
#         with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
#             file.write(new_letter)