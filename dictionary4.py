# Write your max_key function here:
def max_key(my_dictionary):
#Begin by creating two variables named largest_key and largest_value. Initialize largest_value to be the smallest number possible (you can use float("-inf")). Initialize largest_key to any value you want (this will be immediately overwritten once we find the first value later than negative infinity).
    largest_value = float("-inf")
    largest_key = None
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key
# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"