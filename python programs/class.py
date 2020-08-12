class Student:
    def __init__(self,n,c):
        self.name=n;
        self.course=c;
    def display(self):
        print("name=",self.name)
        print("course=",self.course)
    def new(self):
        print("name=Manral")
        print("hey there")
obj1=Student("Mukesh Manral","BCA")
obj2=Student("someone","something")
obj3=Student("hello","everyone")
obj4=Student("","")
obj1.display()
obj2.display()
obj3.display()
obj4.new()
