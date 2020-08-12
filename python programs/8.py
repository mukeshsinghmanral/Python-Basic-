def variable_length(farg,*args):
    print("formal arguments=",farg)
    sum=0
    for i in  args:
        sum=sum+i
    print("sum=",(farg+sum))        
variable_length(10,5)
variable_length(5,6,7,8,9)
