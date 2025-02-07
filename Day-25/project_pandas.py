import pandas as pd
def squirrel_count():
    try:
        data = pd.read_csv("C:/Users/prave/nexusascend/Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250206.csv")


        gray_squirrels = data[data['Primary Fur Color'] == 'Gray']
        red_squirrels = data[data['Primary Fur Color'] == 'Cinnamon']
        black_squirrels = data[data['Primary Fur Color'] == 'Black']

        total_gray_count = len(gray_squirrels)
        total_red_count = len(red_squirrels)
        total_black_count = len(black_squirrels)
        sqr_dict_colour = {
            "Fur Colour": ["Gray", "Red", "Black"],
            "count": [total_gray_count, total_red_count, total_black_count]
        }
        df = pd.DataFrame(sqr_dict_colour)
        df.to_csv("Squirrel count.csv")
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: Empty file.")
    except pd.errors.ParserError:
        print("Error: Parsing error. Check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")
squirrel_count()