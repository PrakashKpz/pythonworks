year=int(input("enter a year"))
result= "leap year" if year%100==0 and year %400==0 else"leap year" if (year%100!=0 and year%4==0) else "not a leap year"
print(result)