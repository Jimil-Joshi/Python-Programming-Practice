import numpy as np


def split(a,k):
    a = a[n:] +a[:n]
    return a


a = [1,2,3,4]
n = 2
print(split(a,n))
