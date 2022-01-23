f = [0,1]
n = int(input("Enter any number: "))
for i in range(2,n):
    

    out = f[i - 1] + f[i - 2]
    f.append(out)
print(f)