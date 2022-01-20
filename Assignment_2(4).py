a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

d = (b**2) - (4*a*c)

plus = (-b + d) / (2*a)
minus = (-b - d) / (2*a)

print(plus, minus)