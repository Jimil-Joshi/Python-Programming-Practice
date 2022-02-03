str = "hello world and practice makes perfect and hello world again"
str = str.split(' ')
str2 = []

for i in str:
    if i not in str2:
        str2.append(i)
str2.sort()
print((' ').join(str2))
