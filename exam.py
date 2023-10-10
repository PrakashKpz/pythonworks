year=int(input("enter a year"))

if(year%100==0 and year %400==0):
    print("the year is leap year")
elif(year%100!=0 and year%4==0):
    print("the year is leap year")

else:
    print("the year is not leap year")
