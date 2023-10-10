f=open("C:/Users/prakash/Desktop/python_work/data.txt","r")
lst=[]
for line in f:
    lst.append(line.rstrip("\n"))
print(lst)
longest_word=max(lst,key=lambda w:len(w)) 
print(longest_word)      