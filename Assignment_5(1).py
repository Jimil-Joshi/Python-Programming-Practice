x = int(input("Enter Any Number: "))
y = int(input("Enter Any Number: "))
def compute_gcp(x, y):

    while(y):
        x,y = y,x % y
    return x
def compute_lcm(x,y):
    lcm = (x*y)//compute_gcp(x,y)
    return lcm


print("The LCM is",compute_lcm(x,y))
