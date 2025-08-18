# aula 1 nomeros complexos
numero1 = 3 + 4 
numero2 = 2 - 1 

print(numero1)
print(numero2)

numero3 = complex(5, -3)
print(numero3)

print(numero1.real)
print(numero1.imag)

# aula 2 conversoes de tipos numericos
numero_int = 10
numero_float = float(numero_int)
print(numero_float)


numero_complexo = complex(numero_float)
print(numero_complexo)

print(10 + 10.4)
print(10 + 10.44)  

# aula 3 oprtadores aritmeticos
a = 10
b = 3 
print(a + b)  # Adição
print(a - b)  # Subtração
print(a * b)  # Multiplicação
print(a / b)  # Divisão
print(a // b) # Divisão inteira
print(a % b)   # Módulo
print(a ** b)  # Exponenciação
# aula 4 ordem de precedencia
print(10 + 2 * 3)  # Multiplicação antes da adição

# aula 4 precedencia de operadores
resultado = 3 + 4 * 5 
print("Resultado:", resultado)  # Multiplicação tem precedência sobre adição

resultado2= (3 + 4) * 5 
print(resultado2)  # Parênteses alteram a precedência

exp = 2 ** 3 ** 2 # 2 **(3 ** 2) é avaliado primeiro
print(exp)  # Exponenciação é avaliada da direita para a esquerda

po_complexas = (10 + 5) * 2 - (33 + 4 /2)
print(po_complexas)  # Avaliação de expressões complexas

# aula 5 - funcoes matematicas
numero = -15

numero_abs = abs(numero)
print("Valor absoluto:", numero_abs)

numero_quebrador = 1.4235437534

print(round(numero_quebrador, 2))  # Arredonda para 2 casas decimais

base = 2 
expoente = 5
modulo = 3

resultado = pow(base, expoente, modulo)
print("Resultado de pow:", resultado)  # Calcula (base ** expoente) % modulo

quociente = divmod(10, 3)
print("Quociente e resto:", quociente)  # Retorna (quociente, resto)