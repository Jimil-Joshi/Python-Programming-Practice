import numpy as np

lower = 1
upper = 10
a = []

for num in range(lower, upper+1):
    if num > 1:


        for i in range(2,num):
            if num%i == 0:
                break

            else:
                a.append(num)


    else:
        print("Number Is Not a Prime Number.")
print(a)
len(a)
