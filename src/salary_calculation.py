hours = 8
hourly_rate = 80
tax_rate = 0.16
consultancy_share = 0.20

def my_monthly_salary(Days):
    try:
        if Days.isdigit():  # Check if the input is a digit
            Days_input = int(Days)  # Convert to integer after the check

            if Days_input > 0:
                gross_salary = Days_input * hours * hourly_rate
                net_salary = gross_salary * (1 - tax_rate)
                my_salary = net_salary * (1 - consultancy_share)
                return my_salary
            elif Days_input == 0:  # Check for zero
                return "Please enter a value greater than zero."
        else:
            return "Please enter a proper value."
    except ValueError:
        return "An error occurred: invalid input."


Days = ""
while Days.lower() != "exit":
    Days = input("Enter the number of days (comma-separated, or type 'exit' to quit):\n")
    total_days = Days.split(", ")
    print(total_days)
    print(set(total_days))
    print(type(set(total_days)))
    if Days.lower() == "exit":
        print("Exiting the program.")
        break

    # Process each number of days from the input
    for num_of_days in set(Days.split(", ")):
        num_of_days = num_of_days.strip()  # Remove any leading/trailing whitespace

        # Call the salary calculation function
        profit = my_monthly_salary(num_of_days)
        print(profit)