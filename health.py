tummy_size=int(input("enter tummy size"))
buttock_size=int(input("enter the buttock size"))
gender=input("enter gender male or female")
measurement=tummy_size/buttock_size
print(measurement)

val=round(measurement,2)

if gender=="male":
    if(val<0.95):

        print("health risk low body shape pear")
    elif(val<1.0):
        print("health moderate low body shape avacado")
    else:
        print("health risk high body shape apple")
elif gender=="female":
    if(val<0.80):
        print("health risk low body shape pear")
    elif(val<0.85):
        print("health risk moderate body shape avacado")
    else:
        print("health risk high body shape apple")
else:
     print("please enter a valid gender")

    