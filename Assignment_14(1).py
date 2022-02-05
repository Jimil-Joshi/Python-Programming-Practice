n = int(input("Enter Any Number:"))

class find_numbers:
    def meth1(self,n):
        try:
            for i in range(0,n):
                if i%7 == 0:
                    print(f"{i} This number is divisible by 7")
                else:
                    print (f"{i} This number is not divisible by 7")
        except e as Exception:
            print(e)
fn = find_numbers()
fn.meth1(n)