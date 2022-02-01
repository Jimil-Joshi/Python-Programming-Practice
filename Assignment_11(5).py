A = "ML an amazing segment of  DS"
B = "Learning ML is needed for DS"
A= A.split(" ")
B= B.split(" ")

def uncommon(A,B):
    for i in A:
        for j in B:
            if i ==j:
                print(i)
uncommon(A,B)
            