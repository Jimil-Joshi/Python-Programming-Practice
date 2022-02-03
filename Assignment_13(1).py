import math

n = input("Enter Any data in coma seprated format: ")
n = n.split(",")
output = []
for d in n:
    q = math.sqrt((2*50*int(d)/30))
    output.append(q)
print(output)

    