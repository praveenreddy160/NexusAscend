import random
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # Example whole numbers

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = ["+", "-", "*", "/", "=", "<", ">", "(", ")", "[", "]", "{", "}", "$", "%", "@", "#", "&", "*", "_",  "!", "?", ".", ",", ":", ";", "'", "\""]


print(f"Hey, User Welcome to the pypassword generator")
user_letters = int(input("how many letters do you like:\n"))
user_whole_number = int(input("how many numbers would you like:\n"))
user_symbol = int(input("how many symbols do you like:\n"))

password = []
for char in range(1, user_letters + 1):   # this char simply holds the value we are using it to just run the loop that many number of times
    password.append(random.choice(letters))
    # print(password)

for char in range(1, user_whole_number + 1):# this char simply holds the value we are using it to just run the loop that many number of times
    password.append(random.choice(numbers))
    # print(password)

for char in range(1, user_symbol + 1):   # this char simply holds the value we are using it to just run the loop that many number of times
    password.append(random.choice(symbols))   # this will actually select the random symbols and then add and store them to the password variable

random.shuffle(password)
new_password = ""
for char in password:
    new_password += str(char)
print(f"your final {new_password} is here")
