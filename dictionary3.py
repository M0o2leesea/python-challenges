# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
#Loop through all values in the dictionary by using for value in my_dictionary.values(). Check to see if value is in my_dictionary.keys() and if so, append it to a list.
    my_list = []
    for value in my_dictionary.values():
        if value in my_dictionary.keys():
            my_list.append(value)
    return my_list
# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]