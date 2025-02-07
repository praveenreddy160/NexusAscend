def leap_year():
    while True:
        year = input("enter a year:\n")
        if year.lower() == "exit":
                break

        if year.isdigit():
            new_year = int(year)
            is_leap_year = (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0)
            if is_leap_year:
                print(f"The {year} is a leap_year")
            else:
                print(f"The {year} is not a leap year")
        else:
                print("Please Enter a Valid Number")

leap_year()
