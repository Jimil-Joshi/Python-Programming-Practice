a = int(input("Enter Any Number: "))

if a > 1:

    for i in range(2, a):
        if a % i == 0:
            print("Number Is Not a Prime Number.")
            break

        else:

            print("Number Is a Prime Number")

else:
    print("Number Is Not a Prime Number.")
