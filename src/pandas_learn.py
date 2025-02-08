import pandas as pd
data = pd.read_csv('weather_data - Sheet1.csv')
# print(type(data))
# print((data['temp'][0]))
temp_list = data['temp'].to_list()
sum = sum(temp_list)
sum1 = len(temp_list)
print(sum1)
# average = sum/len(temp_list)
print(data['temp'].mean())
print(data.condition)
print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data['day'] =='Monday']
monday = data[data.day == 'Monday']
monday_temp = monday['temp']
fahrenheit = (monday_temp * 9/5) + 32
print(fahrenheit)


# Create a data frame from scratch
data_dict = {
    "students": ["Praveen", "Sai", "Arun", "Shashi", "Aditya", "Uday", "dharani"],
    "scores": [76, 56, 65, 78, 89, 90, 76]
}
df = pd.DataFrame(data_dict)
print(df)
df.to_csv("data_dict.csv")


def new_method():
    # In pandas to iterate we have iterrows(): Lets explore
    data_dict = {
        "students": ["Praveen", "Sai", "Arun", "Shashi", "Aditya", "Uday", "dharani"],
        "scores": [76, 56, 65, 78, 89, 90, 76]
    }
    data_dict1 = pd.DataFrame(data_dict)
    # print(data_dict1)

    for (index, row) in data_dict1.iterrows():
        if(row.students) == "Praveen":
            print(row.scores)

new_method()
