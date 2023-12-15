# Write your count_first_letter function here:
def count_first_letter(names):
#Begin by creating an empty dictionary named something like letters. Loop through the keys of names and access the first letter of each the key using key[0].
#If that letter is not a key in letters, create a new key/value pair where the key is key[0] and the value is the length of names[key].
#If that letter is a key in letters, simply add the length of names[key] to value associated with key[0] in letters.
    letters = {}
    for key in names:
        if key[0] not in letters:
            letters[key[0]] = len(names[key])
        else:
            letters[key[0]] += len(names[key])
    return letters
# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}