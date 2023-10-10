from json import load

path="C:\\Users\\prakash\\Desktop\\python_work\\read_fromjson\\data.json"

with open(path) as f:
    records=load(f)

# print(records)

# for f in records:
#     print(f.get("name"))

# fw_names=[f.get("name") for f in records]
# print(fw_names)

top_fw=max(records,key=lambda d:d.get("rating"))
print(top_fw)