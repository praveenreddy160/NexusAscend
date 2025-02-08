import random
names = ['Sai Teja', 'Arun', 'Praveen', 'Uday']
# in dict comprehension it is denoted by {}
student_scores = {student: random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in student_scores.items()if score >=60}
print(passed_students)



sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()  # Split the sentence into a list of words
print(words)

result = {word: len(word) for word in words}
print(result)
# ({word: len(word) for word in words}), """it's necessary to fulfill the key-value structure of dictionaries."""

# change celcius to fahrenheit
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)