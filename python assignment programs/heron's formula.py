import math as m
a=float(input('enter 1 side: '))
b=float(input('enter 2 side: '))
c=float(input('enter 3 side: '))
s=(a+b+c)/2
z=s*(s-a)*(s-b)*(s-c)
if z<0:
	print("Triangle not possible")
else:
	area=m.sqrt(z)	
	print('area:',area)