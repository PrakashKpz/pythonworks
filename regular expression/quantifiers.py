from re import*
text="aabbcaabdaaa"
# pattern="a+"
# pattern="a*"
pattern="a{1,2}"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.group(),m.start())