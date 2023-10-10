text="sunil gavaskar had a n0-holds barred remark on overseas commentators"

vowels=["a","e","i","o","u"]
words=text.split(" ")
for w in words:
    if w[0].casefold()in vowels:
        print(w)