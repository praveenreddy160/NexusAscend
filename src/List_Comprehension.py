word = "PRAVEEN"
result = [word[:i+1] for i in range(len(word))]
for item in result:
    print(item)

new_name = "SAI TEJA"
result = [new_name[:i+1] for i in range(len(new_name))]
print(result)
for k in result:
    print(k)



names = ['roger', 'PPR', 'Praveen', 'Marveler']
note = [name.upper() for name in names if len(name) <6]
print(note)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
print(numbers)
result = [num for num in numbers if num % 2 ==0]
print(result)