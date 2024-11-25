class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
# latte = MenuItem("latte", 200, 300, 250, 3.00)
# price = latte.cost
# print(price)

class Menu:
    """In self attributes we can also give the objects of a different class as value for the attribute value"""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            # print(item.ingredients["item.name"])
            options += f"{item.name}/"
            print(options)
        return options
# new = Menu()
# one = new.get_items()
# print(one)

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name and returns the item if it exists else returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
    
