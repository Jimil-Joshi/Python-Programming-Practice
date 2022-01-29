a = int(input("Enter any number: "))
rem = s = 0
len = len(str(a))
n = a
while(a>0):
    rem =a%10

    s =s + int(rem**len)

    a = a//10

    len = len -1

if s == n:

    print("This Number Is Disarium Number")
else:
    print("This Is Not A Number Disarium Number")
