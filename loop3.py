#Write your function here
def same_values(lst1, lst2):
#Loop through all of the indices of each list using for index in range(len(lst1)) and compare lst1[index] to lst2[index]. Append index to a new list if those two items are equal.
    new_list = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_list.append(index)
    return new_list
#Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))