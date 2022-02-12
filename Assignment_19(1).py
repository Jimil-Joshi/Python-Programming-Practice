a = input("Enter a String: ")


def repeat(a):
    return ''.join([c +c for c in a ])
print(repeat(a))