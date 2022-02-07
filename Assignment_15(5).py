class Shape():
    def __init__(self,length):
        self.length = length
    def area(self,length):
        a = length*length
        print(a)
class sqare(Shape):
    def area2(self,length):
        b = length*length
        print (b)


s = Shape(5)
s2 = sqare(5)

s2.area2(5)
s.area(3)

