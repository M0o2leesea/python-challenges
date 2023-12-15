# Write your add_exclamation function here:
def add_exclamation(word):
#This function should add exclamation points to the end of word until word is 20 characters long. If word is already at least 20 characters long, just return word
#Use a while loop to add exclamation points to word. The while loop should stop when the length of word is greater than or equal to 20.
    while len(word) < 20:
        word += "!"
    return word
# Uncomment these function calls to test your function:
print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn