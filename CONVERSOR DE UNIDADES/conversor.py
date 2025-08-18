# converter Celsius para F
# converter F para C

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit   

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def menu():
    print("Bem-vindo ao conversor de temperatura!")
    print("Escolha uma opção:")
    print("1. Converter Celsius para Fahrenheit")
    print("2. Converter Fahrenheit para Celsius")
    print("3. Sair")

def conversor_temperatura():
    while True:
        menu()
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == '1':
            celsius = float(input("Digite a temperatura em Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius:.2f}°C é igual a {fahrenheit:.2f}°F")
        elif opcao == '2':
            fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit:.2f}°F é igual a {celsius:.2f}°C")
        elif opcao == '3':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Digite 1, 2, ou 3.")

if __name__ == "__main__":
    conversor_temperatura()