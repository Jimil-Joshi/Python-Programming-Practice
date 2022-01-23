


lower = 100
upper = 1000
for a in range(lower,upper+1):
    n = len(str(a))
    temp = a
    sum = 0
    while(temp>0):
        out = temp%10
        sum+= out**n
        temp = temp // 10

    if sum == a:
        print(f"{a} It is an armstrong number.")
    else:
        print(f"{a} It is not an armstrong number.")
