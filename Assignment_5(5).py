a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

opration = input("Which Opration you want to perform? :/n 1.Sum /n 2.Minus /n 3.Multiplication /n 4.Division .")

if opration == '1':
    print("You have selected Sum operation")
elif opration =='2':
    print("You have selected Minus operation")
elif opration =='3':
    print("You have selected Multiplication operation")
elif opration =='4':
    print("You have selected Division operation")
else:
    print("You have not selected valid operation")


def calculation (a,b):
    if opration == '1':
        c = int(a + b)
        return c
    elif opration == '2':
        c = int(a - b)
        return c
    elif opration == '3':
        c = int(a * b)
        return c
    elif opration == '4':
        c = int(a / b)
        return c
    else:
      print("Please select from given choice only")
print(f"Your output of {a} & {b} is {calculation(a,b)} ")