from re import*
# text="abdcdABCDe9fk"
text="abdcdABCDe9#fk_"
# pattern="[0-9]"
# pattern="[a-zA-Z0-9]"
# pattern="[^0-9]"
# pattern="[^a-zA-Z0-9]"
pattern="[AaEeIiOoUu]"
matcher=finditer(pattern,text)
# count=0

# for m in matcher:
#     print(m.start(),m.group())
#     count+=1
# print(count)
for m in matcher:
    print(m.start(),m.group())
