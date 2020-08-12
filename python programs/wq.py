class Myclass:
    __n=0
    @classmethod    
    def __init__(self):
        self.__n+=1
    def noobject():
        print(Myclass.__n)
obj1=Myclass()
obj2=Myclass()
obj3=Myclass()
obj4=Myclass()
Myclass.noobject()

print(obj1._Myclass__n)
