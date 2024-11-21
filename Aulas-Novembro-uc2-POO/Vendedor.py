# Quando estamos criando uma classe, aprimeira coisa é definir uma função __init__
# self transforma a variável em global. Caso não seja definido a ariavel ficará apenas dentro localmente dentro da função.

class Vendedor():
    def __init__(self, nome, vendas):
        self.nome=nome
        self.vendas=vendas

vendedor1 = Vendedor('Raquel', 1000)
print(vendedor1.nome)

