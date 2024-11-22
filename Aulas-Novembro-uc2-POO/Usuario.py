class Usuario():
    def __init__(self, nome, email, cpf, plano, cartaoCredito, fone):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.plano=plano
        self.cartaoCredito=cartaoCredito
        self.fone=fone

usuario1 = Usuario('Raquel','raquel@email.com','91584457')
print(usuario1.telefone)
