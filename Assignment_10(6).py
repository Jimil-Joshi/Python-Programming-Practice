a = [15, 2, 35, 4, 65, 6, 7, 8, 9, 100]
n = 4
b = []
def n_large(a,n):


    max = 0

    for j in range(len(a)):
        if a[j] > max:
            max = a[j]
            a.remove(max)
            b.append(max)
        print(b)
n_large(a,n)


