class Father:
    def __init__(self,p=0):
        self.property=p
    def display(self):
        print("father's property",self.property)
class Son(Father):
    def __init__(self,p=0,p1=0):
        super().__init__(p)
        self.property1=p1
    def display(self):
        super().display()
        print("son's property",self.property1)
        print("combine property",self.property+self.property1)

m1= Son(500000,300000)
m1.display()        
