n = int(input("Enter any Number: "))

def primenumbers(n):
    for i in range(0,n):
        if i%2 == 0:
            print(f"{i} ")
        else:
            print(f"{i} It is not a prime number")
primenumbers(n)
