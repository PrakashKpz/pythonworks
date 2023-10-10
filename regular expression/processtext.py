from re import *
f=("C:/Users/prakash/Desktop/python_work/regular expression/data.txt")
rule1="\d{10}"
rule2="[\w]+@(gmail.com)"
phone_num=[]
email_id=[]
for line in f:
    word=line.rstrip("\n").split()
    for w in word:
        match=fullmatch(rule1,w)
        email_match=fullmatch(rule2,w)
        if match!=None:
            phone_num.append(w)
        elif email_match!=None:
            email_id.append(w)
print(phone_num)
print(email_id)
