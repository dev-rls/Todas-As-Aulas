#App Bancário: 
senha = int(input("Digite sua senha: "))
if senha ==6789:
    print("1.Extrato\n" "2.Depósito\n" "3.Saque\n""4.Sair\n")

extrato= 0.0
opcao=int(input("Escolha uma opção: "))
if opcao == 1:
    print(extrato)

elif opcao == 2:
    deposito=int(input("Digite o valor do seu depósito: "))
    extrato=extrato+deposito
    print(extrato)

elif opcao == 3:
    saque=int(input("Digite o valor do saque: "))
    saque=extrato-saque
    print(extrato)

elif opcao == 4:
 adm=int(input("1.Nome\n" "2.CPF\n" "3.Fone\n""4.Sexo\n"))
 nome=input("Digite seu nome: ")
 cpf=int(input("digite seu cpf: "))
 telefone=int(input("Digite seu telefone: "))

 print(nome)
 print(cpf)
 print(telefone)

elif opcao == 5:
 sair=int(input("Sessão Encerrada"))

else:
     print("Senha Inválida")