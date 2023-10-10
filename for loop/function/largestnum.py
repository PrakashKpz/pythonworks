a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))

def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif(b>a) and (c<a):
        print(b)
    else:
        print(c)

largest(a,b,c)
     