a=input("enter any year :" )
year=int(a)
if year%4==0 :
    print("year is leap")
elif year%100==0 :
    print("year is not leap")
elif year%400==0 :
    print("year is leap")
else :
    print("year is not leap")
