import json

data = None
with open("out.json", "r") as f:
    data = json.load(f)

print(data.keys())
items = data['items']
print(len(items))
for i in items:
    print(i['cardLink'])

data['items'] = []
print(data)