f=open("C:/Users/prakash/Desktop/python_work/data.txt","r")
words=[line.rstrip("\n")for line in f]
longest_word=max(words,key=lambda w:len(w)) 
print(longest_word)      