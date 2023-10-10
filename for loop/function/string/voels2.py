text="what a game, hats of"

vowels=["a","e","i","o","u"]
words=text.split(" ")
for w in words:
    if w[0].casefold()in vowels:
        print(w)