limit=24

prev=0
current=1

print(prev)
print(current)

for i in range(1,limit+1):
    sum=prev+current
    prev=current
    current=sum
    print(sum)
    if sum<=limit:
        print(sum)
    else:
        break