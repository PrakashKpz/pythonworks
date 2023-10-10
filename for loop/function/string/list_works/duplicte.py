lst=[2,2,34,5,5,5,6]
lst.sort()
dupplicate_lst=[]

for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
        if current not in dupplicate_lst:
            dupplicate_lst.append(current)

print(dupplicate_lst)