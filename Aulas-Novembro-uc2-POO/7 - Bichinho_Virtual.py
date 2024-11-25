'''7 - Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico): Atributos: Nome, Fome, Saúde e ldade b. Métodos
Alterar Nome, Fome, Saúde e ldade; Retornar Nome, Fome, Saúde e Idade Obs: Existe mais uma informação que devemos levar em consideração, o
Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja,um campo calculado, então não devemos criar
um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento tem menu de contexto'''

class Tamagushi:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
 
    # Métodos para alterar os atributos
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
 
    def alterar_fome(self, nova_fome):
        self.fome = nova_fome
 
    def alterar_saude(self, nova_saude):
        self.saude = nova_saude
 
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
 
    # Métodos para retornar os atributos
    def retornar_nome(self):
        return self.nome
 
    def retornar_fome(self):
        return self.fome
 
    def retornar_saude(self):
        return self.saude
 
    def retornar_idade(self):
        return self.idade
 
    # Método para calcular o humor
    def calcular_humor(self):
        return (self.saude + (10 - self.fome)) / 2
 
# Exemplos de uso
tamagushi = Tamagushi("Naruto", 5, 8, 2)
 
# Alterar atributos
tamagushi.alterar_nome("Yudi Itadori")
tamagushi.alterar_fome(3)
tamagushi.alterar_saude(10)
tamagushi.alterar_idade(5)
 
# Retornar atributos
print(f"Nome: {tamagushi.retornar_nome()}")
print(f"Fome: {tamagushi.retornar_fome()}")
print(f"Saúde: {tamagushi.retornar_saude()}")
print(f"Idade: {tamagushi.retornar_idade()}")
 
print(f"Humor: {tamagushi.calcular_humor()}") # Calcular humor