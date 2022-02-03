str =  input("enter: ")
d = 0
e = 0

def check(str,d,e):
    for i in str:
        if i.isdigit():
            d = d+1
        elif i.isalpha():
            e = e+1
    print(f"Letters{e}")
    print(f"Numbers{d}")

check(str,d,e)