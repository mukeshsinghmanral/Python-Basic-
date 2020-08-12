class A(object):
    def __init__(self):
        super().__init__()
        print("Class A")
class B(object):
    def __init__(self):
        super().__init__()
        print( "Class B")
class C(B,A,object):
    def __init__(self):
        super().__init__()
        print( "Class C")
c1=C()
