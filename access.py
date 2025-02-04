import os

def save_quote(file_name, quote):
    with open(file_name, "a") as file:
        file.write(f"{quote}")
        print(f"quote successfully saved")

def read_quote(file_name):
    try:
        with open(file_name, "r") as file:
            quotes = file.readlines()
            if quotes:
                print("saved quotes")
                for i, quote in enumerate(quotes):
                    print(f"{i+1}. {quote.strip()}")
            else:
                print(f"No Quotes are saved")
    except FileNotFoundError:
        print("No Quotes saved yet")


def main():
    file_name = "quotes.txt"

    while True:
        print("\nOptions")
        print("1. Save_Quote")
        print("2. read_quote")
        print("3. Exit")
        choice = input("Please Enter Your Choice: ")
        if choice == "1":
            quote = input("Please Enter your Quote: ")
            save_quote(file_name, quote)
        elif choice =="2":
            read_quote(file_name)
        elif choice =="3":
            break
        else:
            print("invalid choice")

if __name__ == "__main__":
    main()


""""Successful"""

