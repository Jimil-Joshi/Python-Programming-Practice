a = "Hello all I am jimil"
d = a.split(" ")
k = 3
c = len(a)
b = []
def length(a, k):
    for i in d:
        if len(i) > k:
            b.append(i)
    return b


length(a,k)
print(b)
