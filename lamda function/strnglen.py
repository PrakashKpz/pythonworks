# get_len=lambda w:len(w)
# print(get_len("hello"))

# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(5,10))

text="hello good morning ziyad"
words=text.split(" ")
# longest_word=max(words,key=lambda w:len(w))
# print(longest_word)

min_word=min(words,key=lambda w:len(w))
print(min_word)