from json import load

path="C:\\Users\\prakash\\Desktop\\python_work\\movies\\mdb.json"
with open(path,encoding="utf 8") as f:
    movies=load(f)

# print("total no of movies",len(movies))
# print(movies)

# fun_movies=[m.get("title")for m in movies if "comedy in m.get"("genres")]
# print(fun_movies)

# lenghty_movie=max(movies,key= lambda m:int(m.get("runtime")))
# print(lenghty_movie)

# genres={g for m in movies for g in m.get("genres")}
# print(genres)

# comedy_movie2015=[m.get("title")for m in movies if "Comedy"  in m.get("genres")and m.get("year")=="2015"]
# print(comedy_movie2015)
wc={}
for m in movies:
    year=m.get("year")
    if year in movies:
        year=m.get("year")
        if year in wc:
            wc[year]+=1
        else:
            wc[year]=1

print(wc)

print(max(wc,key=wc.get("year")))