from re import*
phone=input("enter thr phone number")
rule="\d{10}"
matcher=fullmatch(rule,phone)

if (matcher==None):
    print("invalid")
else:
    print("valid")