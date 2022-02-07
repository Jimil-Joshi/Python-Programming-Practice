n = int (input("Enter any Number: "))

def fibonacci(n):
    values = lambda x: 0 if x==0  else 1 if x==1 else values(x-1)+values(x-2)
    print(','.join([str (values(x)) for x in range (0,n+1)]))

fibonacci(n)