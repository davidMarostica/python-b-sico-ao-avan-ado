# Aula 1 - inteiros 
numero1 = 41 
numero2 = 12

print("Numeros:", numero1, numero2)

print(type(numero1))

valor_absoluto = abs(numero2)
print("Valor absoluto de", numero2, "é", valor_absoluto)

print(pow(numero1, 2)) # potencia

print("Raiz quadrada de", numero1, "é", pow(numero1, 0.5)) # raiz quadrada

print("Soma:", numero1 + numero2)   

# aula 2 operaçoes aritimetica 

a= 20 
b = 7
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a // b # divisão inteira
divisao_normal = a / b
subtracao = a - b
print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão inteira:", divisao)
print("Divisão normal:", divisao_normal)

resto = a % b 
print("Resto da divisão:", resto)

print(2 % 2) # resto da divisão

contador = 10

contador += 10 # contador = contador + 10
print("Contador:", contador)


contador *= 5 
print("Contador após multiplicação:", contador)

contador -= 10
print("Contador após subtração:", contador)
 
# aula 3 - float
temperatura = 32.1
pi = 3.14747474
altura = 1.82

# no exterior, estados unuidos=> , -> . 

print("Temperatura:", temperatura)
print(type(temperatura))

c = 1.8
d = 1.344854385353

print( c + d) # soma de floats
print( c * d) # multiplicação de floats

numero = 1.5e6

print( a + c) # soma de int e float
print( a * c) # multiplicação de int e float

