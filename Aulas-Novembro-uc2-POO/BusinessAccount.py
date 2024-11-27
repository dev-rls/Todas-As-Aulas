from Account import Account

while True:
    tipo=int(input("1 - withdraw , 2 - deposit, 3- loan"))

    if tipo == 1:
        saque = input("Digite o valor do seu saque: ")
        a = Account(saque, 123,0,123)

    if tipo == 2:
        deposito = input("Digite o valor do seu depósito: ")
        b = Account(deposito, 123,0,123)

    if tipo == 3:
        emprestimo = input("Digite o valor do empréstimo: ")
        c = Account(emprestimo, 123,0,123)
        