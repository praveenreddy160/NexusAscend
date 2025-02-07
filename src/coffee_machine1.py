menu = {
"espresso": {
   "ingredients" : {
       "water": 50,
       "coffee": 18,
       },
   "cost": 1.5,
},
"latte": {
   "ingredients" : { 
      "water": 200,
       "coffee": 150,
       "milk": 24,
},
"cost": 2.5,
},
"cappuccino": {
   "ingredients": { 
      "water": 250,
       "coffee": 100,
       "milk": 24,
   },
   "cost": 3.0
}
}
resources = {
    "milk": 300,
    "coffee": 200,
    "water": 300,
}

def reports():
    """Here i'm printing the total available resources after the usage, whenever user needs"""
    print(f"total available water quantity: {resources['water']} in mil")
    print(f"The total available Milk quantity is: {resources['milk']} in mil")
    print(f"the total available coffee in: {resources['coffee']} in gms")


def check_resources(drink):
    """checking if we have enough resources or not"""
    for ingredients, amount in menu[drink]["ingredients"].items():
        if resources[ingredients] < amount:
            print(f"sorry you dont have enough resources: {ingredients}")
            return False
    return True

def process_coins():
    """here i'm prompting the user to enter the number of coins for the coffee"""
    print(f"Hey, User, Please insert the coins for the coffee")
    total = int(input("how many quarters?:\n")) * 0.25
    total += int(input("how many dimes?:\n ")) * 0.1
    total += int(input("how many nickles?:\n ")) * 0.05
    total += int(input("how many pennies?: \n")) * 0.01
    return total

def make_coffee(drink):
    for ingredients, amount in menu[drink]["ingredients"].items():
        resources[ingredients] -= amount
        print("Please enjoy the coffee")

def coffee_machine():
    """this is the main function to simulate the coffee machine"""
    is_on = True
    while is_on:
        choice = input(f"what would you like? Espresso, Latte, cappuccino: \n").lower()
        if choice == "off":
            is_on = False
        elif choice == "reports":
            reports()
        elif choice in menu:
            drink = menu[choice]
            if check_resources(choice):
                payment = process_coins()
                if payment >= drink["cost"]:
                    make_coffee(choice)
                    change = round(payment - drink["cost"], 2)
                    if change > 0:
                        print(f"here is your change for the coffee purchased{change}")
                    else:
                        print(f"Sorry that's not enough money, Money is refunded")
                else:
                    print(f"invalid choice.")

if __name__ == "__main__":
    coffee_machine()