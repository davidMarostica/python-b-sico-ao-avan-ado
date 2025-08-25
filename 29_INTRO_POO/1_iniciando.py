# aula 1 - definicao de classes

# definindo a classe
class Animal:
    # criando a funcao construtora
    def __init__(self, especie):
        # atribuindo valores para as propriedades
        self.especie = especie


animal = Animal("Cachorro")

print(f"Espécie do animal: {animal.especie}")