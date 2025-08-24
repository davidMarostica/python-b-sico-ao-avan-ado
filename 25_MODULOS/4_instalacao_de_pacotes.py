# 1 - instalando pacotes
import requests

response = requests.get("https://api.github.com")

print("Status da req. ", response.status_code)
print("Cabeçalhos: ", response.headers)
