A = "MLan@amazing$segment^ofDS"
special = ["@","_","!","#","$","%","^","&"]

def check_special(A,special):
    for i in A:
        for j in special:
            if i == j:
                print(i)

check_special(A,special)
