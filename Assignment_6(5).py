n = int(input("Enter any number: "))

def sumofcube(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (i * i * i)
    return sum

print(f"Sum of all cube of i is {sumofcube(n)}")
