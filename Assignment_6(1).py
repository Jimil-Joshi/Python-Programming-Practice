def reurssion_fun(n):
    if n<=1:
        return n
    else:
        return (reurssion_fun(n-1)) + (reurssion_fun(n-2))
n_terms = int(input("Enter Any positive  integer number: "))
if n_terms<=0:
    print("Please enter valid positive integer: ")
else:
    for i in range(n_terms):
        print(reurssion_fun(i))
