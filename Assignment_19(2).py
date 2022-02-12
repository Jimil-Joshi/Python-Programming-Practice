a =  input("Enter Boolean: ")
def boolean_reverse(a):
    if a == "True":
        return "False"
    elif a == "False":
        return "True"
    else:
        return "Boolean Expected"
    
print(boolean_reverse(a))