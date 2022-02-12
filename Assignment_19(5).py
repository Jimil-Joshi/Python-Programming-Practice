a =  int(input("Enter:"))
b = []
def prime(a,b):
    for i in range(1,a+1):
        if i %2 ==0:
            b.append(i)
    return b

print(prime(a,b))