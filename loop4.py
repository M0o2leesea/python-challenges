#Write your function here
def reversed_list(lst1, lst2):
#Loop through the numbers created by range(len(lst1)) using a variable named index
#Compare lst1[index] to lst2[len(lst2) - 1 - index]. If those two items are not equal, return False.
    for index in range(len(lst1)):
        if lst1[index]!= lst2[len(lst2) - 1 - index]:
            return False
    return True

#Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))