#Usuario Netflix
class Usuario():
    def __init__(self, nome, email, cpf, plano, cartaoCredito, fone):
        self.nome=nome
        self.email=email
        self.cpf=cpf
        self.plano=plano
        self.cartaoCredito=cartaoCredito
        self.fone=fone

usuario1 = Usuario('Raquel','raquel@email.com',91584457, 'básico', 123, 679999999)
print(f"O plano da {usuario1.nome} é o {usuario1.plano}, telefone:{usuario1.fone}, email: {usuario1.email}..")

usuario2 = Usuario('Eduarda','eduarda@email.com',91584455, 'padrão', 123, 679998889)
print(f"O plano da {usuario2.nome} é o {usuario2.plano}, telefone:{usuario2.fone}, email: {usuario2.email}.")

usuario3= Usuario('Jamily','jamily@email.com',91584477, 'premium', 123, 705070)
print(f"O plano da {usuario3.nome} é o {usuario3.plano}, telefone:{usuario3.fone}, email: {usuario3.email}.")
