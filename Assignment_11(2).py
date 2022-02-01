a = "hellomynameisjimil"
i = 3
def remove_function(a,i):
    for x in range(len(a)):
        if x == i:
            a = a.replace(a[i], "",1)
    return a



print(remove_function(a,i))