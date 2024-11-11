def calculator():
    try:
        number1 = float(input("Hey, User! Please Enter a Valid Number:\n"))
        Operation_method = input("Please Enter a valid Operator:\n")
        number2 = float(input("Hey, User! Please Enter a Valid Second Number:\n"))
        if Operation_method == "+":
            result = number1 + number2
        elif Operation_method == "-":
            result = number1 - number2
        elif Operation_method == "*":
            result = number1 * number2
        elif Operation_method == "/":
            if number2 == 0:
                print(f"Please Enter a Valid Number")
                return
            else:
                result = number1 / number2
        else:
            print("Error: Invalid operator")
            return
        print("result:", result)
    except ValueError:
        print("Error: Invalid input. Please enter only numbers.")
    
calculator()
