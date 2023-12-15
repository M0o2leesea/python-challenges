# Write your check_for_name function here:
def check_for_name(sentence, name):
    return sentence.lower().find(name.lower())!= -1
# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False