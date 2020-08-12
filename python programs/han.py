try:
    f=open('myfile.txt','w')
    a=int(input("Enter a value "))
    b=int(input("Enter a value "))
    c=a/b
    s=f.write(str(c))
    print("Result is stored")
except ZeroDivisionError:
    print( "Division is not possible")
except:
    print("may be divided by double negative sign")

finally:
    f.close()
