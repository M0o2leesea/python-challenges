#Write your function here
def max_num(nums):
#Create a variable called maximum to track the max number, and have it start as the first element in the list. Loop through all of the numbers in the list, and if a number is ever greater than the current max number, the max number should be re-set to that number
    maximum = nums[0]
    for num in nums:
        if num > maximum:
            maximum = num
    return maximum

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))