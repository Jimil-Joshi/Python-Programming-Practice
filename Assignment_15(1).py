n = int(input("Enter Any Number:"))
def divisibleby(n):
    for i in range(0,n):
        if i%5 == 0 and i%7 ==0:
            print(i)

d1 = divisibleby(n)
print(d1)
