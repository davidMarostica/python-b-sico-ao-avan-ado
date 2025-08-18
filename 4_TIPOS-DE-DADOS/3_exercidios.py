# Exercício 1
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

print("Soma:", numero1 + numero2)
print("Subtração:", numero1 - numero2)
print("Multiplicação:", numero1 * numero2)
print("Divisão inteira:", numero1 // numero2)

# Exercício 2
numero_float = float(input("\nDigite um número decimal: "))
numero_arredondado = round(numero_float, 2)
print("Número original:", numero_float)
print("Número arredondado para 2 casas decimais:", numero_arredondado)

# Exercício 3
numero_int = int(input("\nDigite um número inteiro: "))
numero_convertido_float = float(numero_int)
print("Convertido para float:", numero_convertido_float)

numero_float2 = float(input("Digite um número decimal: "))
numero_convertido_int = int(numero_float2)
print("Convertido para inteiro:", numero_convertido_int)

# Exercício 4
import math

print("\nEquação do 2º grau: ax² + bx + c = 0")
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Não existem raízes reais.")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Raiz 1:", raiz1)
    print("Raiz 2:", raiz2)

# Exercício 5
raio = float(input("\nDigite o raio do círculo: "))
area = math.pi * (raio ** 2)
print(f"A área do círculo é: {area:.2f}")