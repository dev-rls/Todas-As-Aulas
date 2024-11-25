class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.crescer(0.5)

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, {self.peso} kg, {self.altura} cm."

pessoa = Pessoa("Raquel", 31, 56, 162)
# pessoa.envelhecer()
# pessoa.emagrecer()
# pessoa.crescer()
print(pessoa)
