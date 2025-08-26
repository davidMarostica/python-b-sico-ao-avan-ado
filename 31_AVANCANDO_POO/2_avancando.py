# aula 1- MRO
class A:
    def acao(self):
        print("Acao A")

class B(A):
    def acao(self):
        print("Acao B")

class C(A):
    def acao(self):
        print("Acao C")

class D(B, C):
    pass


obj = D()

obj.acao()

print(D.mro())


# super

class X:
    def fazer_algo(self):
        print("Fazendo algo em X")


class Y(X):
    def fazer_algo(self):
        super().fazer_algo()
        print("Fazendo algo em Y")

obj2 = Y()

obj2.fazer_algo()

class Z(Y):
    def fazer_algo(self):
        super().fazer_algo()
        print("Fazendo algo em Z")

obj3 = Z()

obj3.fazer_algo()