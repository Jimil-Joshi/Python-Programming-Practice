def pronic(n):
    flag = False
    for i in range(1,n+1):
        if(i*(i+1)) == n:
            flag = True
            break
    return flag
for j in range(1,100):
    if pronic(j):
        print(j)

