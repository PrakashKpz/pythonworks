# prgm1:
num=int(input("enter the number:"))

if num>=10 and num<=20:
    print("Thank You")
else:
    print("incorrect")

# prgm2:
num=int(input("enter the number:"))
if num<10:
    print("Too low")
elif num>=10 and num<=20:
    print("Correct")
else:
    print("Too high")

# prgm3:
age=int(input("enter the age:"))

if age>=18:
    print("You can vote")
elif age==17:
    print("you can learn to drive")
elif age==16:
    print("ypu can buy the lottery ticket")
elif age<16:
    print("you can go for treat")

# prgm4:
num=int(input("enter the num 1 or 2 or 3:"))
if num==1:
    print("Thank you")
elif num==2:
    print("Well done")
elif num==3:
    print("Correct")
else:
    print("Error message")

# prgm5:
num=int(input("enter the num:"))

if num%2==0 and num%3==0:
    print("num divisible by both 2 and 3")
else:
    print("not divisible")

# prgm6:
character="i"

if character in ["a","e","i","o","u"]:
    print("vowel")
else:
    print("not")

# prgm7:
num=int(input("enter the number:"))
for i in range(1,11):
    mul=num*i
    i+=1
    print(mul)

# prgm8:
num=int(input("enter the number:"))

for i in range(1,num+1):
    if i%2==0:
        print(i)
    i+=1

# prgm9:
text=input("enter the name=>")
start=1

while(start<=3):
    print(text)
    start+=1

# prg10:
name=input("enter the name=>")
num=int(input("enter the number:"))


if num<10:
    for i in range(1,num+1):
        print(name)
        i+=1
else:
    print("too high")

# prgm11:
num=int(input("Enter number of person wants to invite the party:"))
if num<10:
    for i in range(1,num+1):
        name=input("Enter the name>")
        print(name,"has been invited")
else:
    print("Too many peoples")

# prgm12:
number = 0

while number <= 5:
    number = int(input("Enter a number : "))
print("The last number you entered was a ",number)

# prgm13:
num=int(input("enter a number between 10 and 20:"))

while num<10 or num>20:
    if num<10:
        print("too low")
    else:
        print("too high")
    num=int(input("enter a number between 10 and 20:"))
print("thank you")

# prgm14:
num=int(input("enter the number:"))

for i in range(10,num+1):
    print(i)
    i+=1

# prgm15:
average=0
for i in range(1,6):
    num=int(input("enter the number:"))
    average+=num
print(average)
