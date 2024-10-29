def tip_calculator():
        while True:
            print(f"welcome to the Tip Calculator!")
            total_bill = input("Hey User, Please enter your total bill:\n")
            if not total_bill.replace('.', '', 1).isdigit():
                    print(f"Please enter a valid amount")
                    continue
            
            Tip = input("Hey, User what's the tip amount you wanted to provide:\n")
            if not Tip.replace('.', '', 1).isdigit():
                print(f"Please enter a valid  tip amount")
                continue

            Each_person = input("Hey, User Please enter the total number of people to split:\n")
            if not Each_person.isdigit():
                        print(f"Please Enter Valid number of people:\n")
                        continue
            new_bill = float(total_bill)
            new_tip = float(Tip)
            Total_people = int(Each_person)

            tip_amount = new_bill * (new_tip / 100)
            Final_Bill = round(new_bill + tip_amount, 2)
            Split_Share = round(Final_Bill / Total_people, 2)

            print(f"Hey, User! the final bill is ready {Final_Bill:.2f} Dollars and each person's share will be {Split_Share:.2f} Dollars. Thanks!")
            break

tip_calculator()


