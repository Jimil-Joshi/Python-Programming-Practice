a = int(input("enter any number: "))

n = a
rem = s = 0


while(a!=0):
    rem = a%10
    s = s+rem
    a=a//10

if  n%s == 0:
    print("It is a Harshad Number")
else:
    print("Sorry")



