
from Cadastro import Cadastro, PFisica, PJuridica

while True:
    tipo=int(input("1 - Pessoa Física\n2 - Pessoa Jurídica\nInsira sua opção: "))

    if tipo == 1:
        pf = PFisica()
        pf.PF()
        
    if tipo == 2:
        pf = PJuridica()
        pf.PJ()
        
    else:
        print("Opção Inválida")