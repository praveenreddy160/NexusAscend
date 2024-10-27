def student_info():
    Student = {
    "name": "Roger",
    "age": 27,
    "college": "University of Texas at Arlington",
    "Gender": "Male"
    }
    Student.update({
        "height": 5.8,
        "weight": "180lbs",
        "name": "Maverick"
    })

    print(type(Student))
    print(Student)

student_info()

# here i'm using the nested dictionary

def roomies():
    roomates = {
        "name": "Maverick",
        "age": 28,
        "address": "Tempe",
        "modus": "rent",
        "neighbour": {        
            "name": "oldman",
            "age": "68",
            "city": "tempe",
            "modus": "owner"
        }

    }
    roomates.update({"modus": "cash"})
    roomates["neighbour"].update({"HOA": "Member"})
    for roomie, values in roomates.items():
        print(f"my room_mate {roomie} is {values}")
        if isinstance(values, dict):
            for sub_roomie, sub_values in values.items():
                print(f"my neighbour {sub_roomie} is {sub_values}" )

roomies()

# in the dict we have update method from which we can update, add, merge two dictionaries etc
#  in dict we can access nested dicts by dict_name["dict_name2"]