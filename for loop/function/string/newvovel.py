text="Eight five six out"

vowels=["a","e","i","o","u"]
words=text.split(" ")
for w in words:
    if w.casefold().startswith(vowels): 
        print(w)