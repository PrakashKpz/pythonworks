f_news=open("C:\\Users\\prakash\\Desktop\\python_work\\tokenization\\stopword.txt")
f_stop=open("C:\\Users\\prakash\\Desktop\\python_work\\tokenization\\news.txt")
stop_words={line.rstrip("\n")for line in f_stop}
news_set=set()
for line in f_news:
    words=line.split()
    for f in words:
        news_set.add(w)

print(news_set.difference(stop_words))