class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def inner(self):
        self.l1=self.Laptop('HP','8gb','ryzen 5')
        self.l2=self.Laptop('Dell','4gb','i5')
    def show(self):
        print(self.name,self.rollno)
    class Laptop:
        def __init__(self,brand,ram,cpu):
            self.brand=brand
            self.ram=ram
            self.cpu=cpu
        def show(self):
            print(self.brand,self.ram,self.cpu)
            
s1=Student("Mukesh Manral",46)
s2=Student("xyz",32)
s1.show()
s1.inner()
s1.l1.show()
s2.show()
s2.inner()
s2.l2.show()
