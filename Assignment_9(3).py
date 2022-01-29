a = int(input("Enter Any Number: "))
rem = s = 0
res = a


def happy_number(a):
    while (a>0):
        rem = a%10
        s=rem**2
        a//=10
    return s
while(res!=1 and res!=4):
    res = happy_number(res)


if res == 1:
    print("This is a Happy Number.")
elif res == 4:
    print("This is not a Happy Number.")
