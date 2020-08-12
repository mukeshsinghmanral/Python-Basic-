import functools 
List=[2,4,3,5,6,7,8,9,10]
lists=list(filter(lambda x:x%2==0,List))
doubles=list(map(lambda n:n*2,lists))
print(doubles)
sum=functools.reduce(lambda x,y:x+y,doubles)
print(sum)
