# Write your remainder function here:
def remainder(num1, num2):
#Multiply the first input value by 2
  return num1 * 2 % num2
#Divide the second input value by 2
  return num2 / 2 % num1
#Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
  return remainder(num1, num2)
#Return the answer

# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0