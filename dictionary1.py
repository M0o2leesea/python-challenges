# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
#Create a counter variable and start it at 0. Loop through all of the elements of the keys of the dictionary by using my_dictionary.keys(). If the key is even (which you can check by using key % 2 == 0), add the corresponding value to the counter.
    counter = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            counter += my_dictionary[key]
    return counter
# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6