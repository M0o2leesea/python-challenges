# Write your count_multi_char_x function here:
def count_multi_char_x(word, x):
#For example, count_multi_char_x("Mississippi", "iss") should return 2
#Consider using the split function. How does the length of word.split(x) relate to the number of times x was in word?
    split_word = word.split(x)

    return (len(split_word)-1)
# Uncomment these function calls to test your function:
print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1