all_users=["sachin","dhoni","kohli","rohit","sanju","paikl"]
sanju_following=["padikl","sachin"]

suggestion_set=list(set(all_users).difference(set(sanju_following)))
sanju_pos=suggestion_set.index("sanju")
suggestion_set.pop(sanju_pos)
print(suggestion_set)