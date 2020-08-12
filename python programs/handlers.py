a=int(input("enter any number:"))
b=int(input("enter any number:"))
try:
    c=a/b
except ArithmeticError as m:
    print(m)
    print("you can divide by any natural no.")
    
    b=int(input("enter divisor again except 0:"))
    c=a/b
finally:
    print(c)
