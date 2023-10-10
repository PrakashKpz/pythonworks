from json import load
path="C:\\Users\\prakash\\Desktop\\python_work\\countries\\countries.json"
with open(path,encoding="utf-8")as f:
    countries=load(f)
# starts_withc=[c.get("name")for c in countries if c.get("name").startswith("C")]
# print(starts_withc)

# c_with_boders=[c for c in countries if "borders" in c]
# max_border_country=max(c_with_boders,key=lambda c:len(c.get("borders")))
# print(max_border_country.get("name"))

# india_borders=[c.get("borders")for c in countries if c.get("name")=="India"][0]
# india_border_names=[c.get("name")for c in countries if c.get("alpha3code") in india_borders]
# print(india_border_names)

all_region={c.get("region") for c in countries}
# print(all_region)

depended_countries=[c.get("name") for c in countries if c.get("independent")==False]
# print(depended_countries)

popl_filter=[c.get("name") for c in countries if c.get("population") <400000]
print(popl_filter)
