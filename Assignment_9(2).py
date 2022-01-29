
def range_num (a):
    rem = s = 0
    length = len(str(a))
    n = a
    while(a>0):
        rem =a%10
        s += int(rem**length)
        a = a//10
        length = length - 1
    return s
result = 0

for a in range(1,100):
    result = range_num(a)

    if result == a:
        print(a)


