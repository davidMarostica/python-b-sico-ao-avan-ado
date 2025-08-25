# aula 1 - excecoes personalizadas
class UsuarioNaoEncontradorError(Exception):
    pass

try:
    if 1 == 1:
        raise UsuarioNaoEncontradorError("Usuário não encontrado no sistema...")
except UsuarioNaoEncontradorError as e:
    print(f"Erro: {e}")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        super().__init__(f"Saldo insuficiente. Você tentou sacar R${valor} e só R${saldo} na conta")

try:
    saldo = 50
    valor = 100

    if valor > saldo:
        raise SaldoInsuficienteError(saldo, valor)
except SaldoInsuficienteError as e:
    print(e)
