f=open("C:/Users/prakash/Desktop/python_work/numbers.txt", "r")
numbers=[line.rstrip("\n") for line in f]
for n in numbers:
    if n.startswith("kl"):
        print(n)