# Write your substring_between_letters function here:
def substring_between_letters(word, start, end):
#Begin by finding the indices of the start and end characters by using word.find(start) and word.find(end).
    word_indices = word.find(start)
    end_indices = word.find(end)
#If either of those indices are -1, then the original string didn’t contain one of those characters, and you should return words.
    if word_indices == -1 or end_indices == -1:
        return word
    else:
        return word[word_indices+1:end_indices]

# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"