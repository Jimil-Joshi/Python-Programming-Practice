a = "Hello World"
a = list(a)

def Reverser(a):
    b = len(a)
    for i in range (b):
        if a[i]>='a' and a[i]<='z':
            a[i] =chr(ord(a[i])-32)
        elif a[i] >= 'A' and a[i] <= 'Z':
                a[i] = chr(ord(a[i]) + 32)
    return a[::-1]

Reverser(a)

a= ''.join(a)
print(a[::-1])