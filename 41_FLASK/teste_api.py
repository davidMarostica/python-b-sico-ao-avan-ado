import requests

# URL base da API
BASE_URL = "http://127.0.0.1:5000/api"

# Testando método GET
print("=== TESTANDO GET ===")
res = requests.get(BASE_URL)
print(f"Status Code: {res.status_code}")
print(f"Resposta: {res.json()}")
print()

# Testando método POST
print("=== TESTANDO POST ===")
res = requests.post(BASE_URL)
print(f"Status Code: {res.status_code}")
print(f"Resposta: {res.json()}")
print()

# Testando método PUT
print("=== TESTANDO PUT ===")
res = requests.put(BASE_URL)
print(f"Status Code: {res.status_code}")
print(f"Resposta: {res.json()}")
print()

# Testando método DELETE
print("=== TESTANDO DELETE ===")
res = requests.delete(BASE_URL)
print(f"Status Code: {res.status_code}")
print(f"Resposta: {res.json()}")
print()

# Testando POST com dados JSON
print("=== TESTANDO POST COM DADOS ===")
dados = {"nome": "João", "idade": 30}
res = requests.post(BASE_URL, json=dados)
print(f"Status Code: {res.status_code}")
print(f"Resposta: {res.json()}")