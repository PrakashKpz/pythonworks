lst=[10,11,10,11,12,13]
lst.sort()
duplicate_lst=[]

for i in range(0,len(lst)-1):
    current=lst[i]
    next=lst[i+1]
    if current==next:
        if current not in duplicate_lst:
            duplicate_lst.append(current)

print(duplicate_lst)