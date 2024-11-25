'''4 - Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: n° conta da conta, nome do correntista, e saldo. Os
métodos são os seguintes: alterar nome, depósito e saque. No construtor, saldo é opcional, com valor defalt zero e os demais atributos são obrigatórios.
'''
class Conta_Corrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
       
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
 
    def alterar_nome(self, novo_nome):
       
        self.nome_correntista = novo_nome
        print(f"Nome alterado para {self.nome_correntista}")
 
    def deposito(self, valor):
       
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")
 
    def saque(self, valor):
   
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")
 
 
conta1 = Conta_Corrente(678910, "Raquel Santos")
conta1.deposito(1000)
conta1.saque(200)
conta1.alterar_nome("Raquel Lemos")