# Letters = ['a', 'b', 'c', 'd']
# new_form = '-'.join(Letters)
# print(new_form)




def calculate_love_score(name1, name2):

    # Combined the names and convert to lowercase
    combined_names = name1.lower() + name2.lower()
    
    # Initializing counters for TRUE and LOVE letters
    true_count = 0
    love_count = 0

    # Count occurrences of letters in "TRUE"
    for letter in "true":
        true_count += combined_names.count(letter)

    
    for letter in "love":
        love_count += combined_names.count(letter)

    score = int(str(true_count) + str(love_count))
    
    print(f"Your love score is {score}")


calculate_love_score('Kanye West', 'Kim Kardashian')
