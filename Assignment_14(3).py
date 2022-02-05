class main:
    pass
class male(main):
    def getGender(self):
        print("Male")

class female(main):
    def getGender(self):
        print("Female")
        male.getGender(self)

f = female()
f.getGender()