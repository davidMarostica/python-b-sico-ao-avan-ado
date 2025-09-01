import requests

# Testar todos os métodos
base_url = "http://127.0.0.1:5000/api"

# GET
res = requests.get(base_url)
print(f"GET - Status: {res.status_code}, Response: {res.json()}")

# POST
res = requests.post(base_url)
print(f"POST - Status: {res.status_code}, Response: {res.json()}")

# PUT
res = requests.put(base_url)
print(f"PUT - Status: {res.status_code}, Response: {res.json()}")

# DELETE
res = requests.delete(base_url)
print(f"DELETE - Status: {res.status_code}, Response: {res.json()}")