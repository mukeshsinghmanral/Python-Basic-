import math as m
x1,y1,x2,y2=int(input('enter x coordinate of 1st point: ')),int(input('enter y coordinate of 1st point: ')),int(input('enter x coordinate of 2nd point: ')),int(input('enter y coordinate of 2nd point: '))
d=m.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
print('distance between',(x1,y1),'and',(x2,y2),'is: ',d)