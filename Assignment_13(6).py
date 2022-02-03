import re

username = input("Enter username: ")
password = input("Enter password: ")
password = password.split(",")

validpassword = []

for i in password:
    if not re.search ("([a-z])",i):
        continue
    elif not re.search ("([0-9])",i):
        continue
    elif not re.search("([A-Z])", i):
        continue
    elif not re.search("([$#@])", i):
        continue
    elif len(i) <6 or len(i) >12:
        continue
    else:
        validpassword.append(i)
print((" ").join(validpassword))
    

