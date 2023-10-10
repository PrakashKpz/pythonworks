# def max_word(*args):
#     lengthy_word=max(args,key=lambda w:len(w))
#     return lengthy_word

# print(max_word("hello","goodmrng","hi"))
    

def display_emp(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("salary"))

display_emp(name="hari",dept="cse",place="ekm",salary="4000")
    