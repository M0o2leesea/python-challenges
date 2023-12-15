#Write your function here
def over_nine_thousand(lst):
    sum = 0
# Loop through all of the elements of lst and use a break when the sum is greater than 9000.
    for i in lst:
        sum += i
        if sum > 9000:
            break
    return sum
    

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))