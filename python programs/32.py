class Secretvar:
    __secretcount=0
    def count(self):
        self.__secretcount+=1
        print(self.__secretcount)
counter=Secretvar()
counter.count()
counter.count()
print(counter._Secretvar__secretcount)
