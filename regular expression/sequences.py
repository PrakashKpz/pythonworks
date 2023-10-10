from re import*
text="abcd12kABC@#"
# pattern="\d"
# pattern="\D"
# pattern="\w"
# pattern="\W"
pattern="[^aeiou\W\d]"
matcher=finditer(pattern,text)

for m in matcher:
    print(m.group(),m.start())