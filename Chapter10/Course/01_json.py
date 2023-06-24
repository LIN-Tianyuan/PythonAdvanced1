import json
data = [{"name": "Kevin", "age": 16}, {"name": "Laurent", "age": 20}]

# Convertir les données python en données json
data = json.dumps(data)
print(data)

# Convertir les données json en données python
data = json.loads(data)
print(data)