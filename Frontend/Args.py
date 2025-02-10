# def add(*args):
#     sum = 0 # intialise very important
#     for n in args:
#         sum += n
#     print(sum)
# add(2, 3, 4, 5, 6)
# # print(new_value)


def calculate(**kwargs):
    # print(kwargs)
    n = 0
    # for key, value in kwargs.items():
    #     # print(key)
    #     # print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    # print(n)
   

calculate(add= 5, multiply = 6)


def create_user_profile(user_name, **kwargs):
    profile = {"user_name": user_name}
    profile.update(kwargs)
    return profile
user1 = create_user_profile('Praveen', age = 27, gender = 'male', Profession = 'Software Developer- I', company = 'Fannie Mae')
print(f"Hi, my name is {user1['user_name']} and I'm {user1['age']} years old and I'm a {user1['Profession']} at {user1['company']}")
user2 = create_user_profile('Marveler', age = 28, gender = 'Male', Profession = 'Python Developer')

# so in classes
class Car:
    def __init__(self, **kw):
      self.make = kw['Make']  
      self.Year = kw.get('Year')
      self.model = kw['Model']
      self.owner = kw.get('Owner')
    
    def my_variable_data(self):
        print(f" And I have a New {self.make} {self.model} {self.Year}")

car_object = Car(Make = 'Honda', Year = '2025', Model = 'CR-V', Owner = 'Praveen Reddy')
car_object.my_variable_data()