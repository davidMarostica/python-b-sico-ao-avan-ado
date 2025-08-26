# aula 1 - metodos estáticos

class Validator:
    @staticmethod
    def validar_idade(idade):
        return idade > 0
    
print(Validator.validar_idade(10))
print(Validator.validar_idade(-5))

class Matematica:
    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def calcular_area_retangulo(base, altura):
        return base * altura
    
    def soma2(self, a, b):
        return a + b
    

print(Matematica.soma(10, 2))

print(Matematica.calcular_area_retangulo(12, 5))

# print(Matematica.soma2(10, 2)) -> erro, precisa de objeto
