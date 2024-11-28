"""Desenvolva uma classe super que conterá dados de cadastro comuns, como nome, endereço, fone, entre outros(10 dados)

Em seguida desenvolva uma outra classe que conterá dados pertinentes a pessoa física(5 dados)
Posteriormente desenvolva uma outra classe que conterá dados pertinentes a pessoa jurídica(5 dados)

Instancie essas classes onde você deverá pedir os dados comuns e caso seja pessoa física, chamar a classe PF. caso contrário PJ"""

class Cadastro: #Super
    def __init__(self):
        self.nome = (input("Digite o seu nome: "))
        self.dataDeNas = (input("Digite sua data de nascimento: "))
        self.sexo = (input("Digite o seu sexo: "))
        self.fone = (input("Digite o seu telefone: "))
        self.email = (input("Digite o seu email: "))
        self.endereco = (input("Digite o seu endereço: "))
        self.cidade = (input("Digite sua cidade: "))
    
class PFisica(Cadastro):
    def PF(self):
        self.cpf= (input("Insira seu CPF: "))
        self.estCivil = (input("Digite seu estado civil: "))
        self.rg = (input("Digite o seu rg: "))

class PJuridica(Cadastro):
    def PJ(self):
        self.empresa= (input("Digite o nome de sua empresa: "))
        self.cnpj= (input("Insira seu CNPJ: "))
        self.razSocial(input("Digite a razão social: "))