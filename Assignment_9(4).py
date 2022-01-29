def happy_num(a):
    rem =s =0
    while (a>0):
        rem = a%10
        s = s + (rem*rem)
        a= a//10
    return s

for i in range(1,101):
    res = i

    while (res!=1 and res!=4):
        res = happy_num(res)
    if (res == 1):
      print(i)