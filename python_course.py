# printing the len of input and also having the input in the print function
print(len("Hello " + input("Please enter your name:\n") + "!"))

# # project-1 Band Generator taking the input from the user and printing the band name 
print("welcome to the Band Name Generator.")
city = input("enter the city where you are born?\n")
pet = input("enter your pet name?\n")
print("your band name might be: " + city + " " + pet)


# So this method of pulling out a particular element from a string is called subscripting, and the number and we can use negative number also
print("Hello"[0])
print("Hello"[-1])
# type checking
print(type("Hello"))
print(type(1))
print(type(True))
print(type(1.23))


name = input("please enter your name:\n")
length_of_name = len(name)
print("number of letter's in your name: " + str(length_of_name))


print("my age is: " + str(12))
print(5 / 3) 
print(5 // 3)  # this will leave no reminder
print(2 ** 3) # 2 to the power of 3 exponential


height = 1.65 
weight = 84

# # Write your code here.
# # Calculate the bmi using weight and height.
bmi = weight / (height ** 2)
# # if you give // no reminder and if we use int then we are printing only the value with out no reminder
# # And this is a programming term for basically just removing all of the remaining decimal places, flooring (whole number) and we can also do round

print(int(bmi))
print(round(bmi))


num = 12.59789
# print(round(num)) #it will round of numbers if its more than 0.5 then it will print the 13 instead of 12 if it is 12.6
# print(round(num, 2)) #this will round of to 2 number ex: 12. 32 if it has 12.346
num += 1
print(num)


def odd_or_even():
    number_to_check = int(input("Please enter the number to check even or odd:\n"))
    if number_to_check % 2 == 0:
        print("the number you have entered is an even number")
    else:
        print("the number you have entered is an odd number")

odd_or_even()
                          



