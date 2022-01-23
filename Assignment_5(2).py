x = int(input("Enter Any Number: "))
y = int(input("Enter Any Number: "))

def hcf_find(x,y):
    if x>y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf
hcf = hcf_find(x,y)

print(f"The HCF is {hcf}")
