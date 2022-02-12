String = input("Enter:  ")
String = list(String)
b = []
def string(String,b):
    c = len(String)
    for i in range(c):
        if String[i] >= 'A' and String[i] <= 'Z':
            b.append((String([i])))
    return b.index(i)
print(string(String,b))
