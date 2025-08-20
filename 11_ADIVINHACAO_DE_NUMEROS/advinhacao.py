# ...existing code...
import random

def jogo_advinhacao():
    print("Bem-vindo ao Jogo da Advinhação")
    print("Tente advinhar um número aleatório de 1 a 100!")

    numero_secreto = random.randint(1, 100)
    tentativas = 0
    tentativas_maximas = 7  # Defina o limite de tentativas
    acertou = False

    while not acertou and tentativas < tentativas_maximas:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(f"Parabéns, você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
            acertou = True
        elif palpite < numero_secreto:
            print("O Número secreto é maior. Tente novamente")
        else:
            print("O Número secreto é menor. Tente novamente")

        print(f"Tentativas restantes: {tentativas_maximas - tentativas}")

    if not acertou:
        print(f"Game Over! O número secreto era {numero_secreto}.")

# Inicializar o programa
if __name__ == "__main__":
    jogo_advinhacao()