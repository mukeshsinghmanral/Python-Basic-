class Father:
    def height(self):
        self.height="5 foot 8 inches"
        print("height",self.height)
class Mother:
    def eyecolor(self):
        self.color="Brown"
        print("eye color",c.color)
class Son(Father,Mother):
    def hair(self):
        self.hair="Brown"
        print("hair color",c.hair)
    def display(self):
        super().height()
        super().eyecolor()
        self.hair()       
c=Son()
c.display()
