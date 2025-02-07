student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    print(student_scores)
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
    

print(student_grades)


def travel_log():
    travel = {
        "City": ["Paris", "Nice", "Strasbourg"],
        "Person": {
            "Name": ["Roger", "Martian", "Punk"]
        }
    }
    print(travel["City"][1])
    print(travel["Person"]["Name"][2])

travel_log()