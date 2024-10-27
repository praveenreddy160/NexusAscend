class Car:
    def __init__(self, car_manufacturer, model, year, owner, finance, interest_rate):
        self.car_manufacturer = car_manufacturer
        self.model = model
        self.year = year
        self.owner = owner
        self.finance = finance
        self.interest_rate = interest_rate

    def my_car_details(self):
        print(f"there is a {self.car_manufacturer} {self.model} {self.year} car and the owner is {self.owner}")

    def my_interest_rate(self,new_interest_rate):
        self.interest_rate = new_interest_rate

    def new_interest_rate(self):
        print(f"{self.interest_rate}")

car_info = Car("Honda", "CR_V Hybrid", 2025, "Lord Balaji", "Honda Financial", 6.9)
car_info.my_car_details()
car_info.my_interest_rate(5.9)
car_info.new_interest_rate()
