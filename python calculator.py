def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
x=float(input("enter the first number"))
y=float(input("enter the 2nd number"))
operator=input("enter the operator (+,-,*,/)")
if operator=="+":
    print(x,'+',y ,"=" ,add(x,y))
elif operator=="-" :
    print(x,"-",y,"=",sub(x,y))
elif operator =="*":
    print( x,"*",y,"=",multiply(x,y))
elif operator =="/" :
    print( x,"/",y,"=",divide(x,y))
else:
    print("invalid operation")


