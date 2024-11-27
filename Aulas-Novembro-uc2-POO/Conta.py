from Conta_Bancaria import Conta
  
while True:
    tipo=int(input("1 - cadastro"))

    if tipo == 1:
        nome = input("Digite seu nome: ")
       
        x = Conta(nome, 123,0,123)
 