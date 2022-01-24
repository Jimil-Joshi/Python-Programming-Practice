
n = int(input("Enter any Number: "))
def recur_fun(x):
    if x==1:
        return x
    else:
        return (x*(recur_fun(x-1)))

print(f"Factorial of {n} is {recur_fun(n)}")

