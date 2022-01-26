a = [6,3,5,1,4,2,0]
n = len(a)

def monotone(a,n):
    if n == 1:
        return True
    else:
        # check for monotone behaviour
        if all(a[i] >= a[i + 1] for i in range(0, n - 1) or a[i] <= a[i + 1] for i in range(0, n - 1)):
            return True
        else:
            return False
print(monotone(a,n))