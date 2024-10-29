def calculate_pizza_bill():
  """It will Calculate the final bill for a pizza order based on user preferences."""

  print("Welcome to Python Pizza Deliveries!")
  size = input("What size pizza do you want? S, M, or L: ")
  add_pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
  extra_cheese = input("Do you want extra cheese? Y or N: ")

  bill = 0

  if size == "S":
    bill += 15
    if add_pepperoni == "Y":
      bill += 2
  elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
      bill += 3
  elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
      bill += 3
  else:
    print("Invalid pizza size entered.")
    return

  if extra_cheese == "Y":
    bill += 1

  print(f"Your final bill is: ${bill}")

calculate_pizza_bill()