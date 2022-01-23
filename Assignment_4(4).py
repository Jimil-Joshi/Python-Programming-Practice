a = int(input("Enter any number: "))
n = len (str(a))
temp = a
sum = 0

while(temp>0):
    out = temp%10
    sum+= out**n
    temp = temp // 10

if sum == a:
    print("It is an armstrong number.")
else:
    print("It is not an armstrong number.")
