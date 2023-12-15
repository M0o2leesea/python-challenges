#Write your function here
def larger_sum(lst1, lst2):
#Create variables named sum1 and sum2 and set them to be 0. 
# Loop through each list separately and add to the appropriate variable. 
# After looping through each list, compare the two sums in an if statement and return the correct list.
    sum1 = 0
    sum2 = 0
    for index in range(len(lst1)):
        sum1 += lst1[index]
        sum2 += lst2[index]
        if sum1 > sum2:
            return lst1
        elif sum1 < sum2:
            return lst2
        

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))