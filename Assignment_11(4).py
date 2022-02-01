a = "101010101010101010"

b =  "my name is jimil"

def string_check(a):
    p = set(a)
    x = {'0','1'}
    if p ==x or p =='0' or p =='1':
        print("Yes")
    else:
        print("No")
        
string_check(a)