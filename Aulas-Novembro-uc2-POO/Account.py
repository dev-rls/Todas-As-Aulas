'''Vamos impletar as classes Account e BussinessAccount e fazer alguns testes '''
class Account:
    def __init__(self, number:int,holder:str, balance: float):
        self.number=number    
        self.holder=holder
        self.balance=balance

    def withdraw(self, amount: float): #saque
        if amount > 0:
            self.balance += amount

    def deposit(self,amount:float ): #depositar
        if amount > 0:
            self.balance -= amount
        else:
            print("Valor inválido")

    def __str__(self):
        return f"Conta({self.number}, {self.holder},balance: {self.balance:.2f})"

class BusinessAccount(Account):
    def __init__ (self, number:int, holder:str, balance:float, loanLimit:float):
        super().__init__(number, holder, balance)
        self.loanLimit = loanLimit
    
    def loan(self, amount:float): #emprestimo
        if amount > 0 and amount <= self.loanLimit:
            self.balance+= amount
            self.loanLimit = self.loanLimit

        else:
            print("Emprestimo excede o limite permitido")
            
    def __str__(self):
        return f"Busines Conta({self.number}, {self.holder},balance: {self.balance:.2f}, loanLimit: {self.loanLimit})"
    acc = Account(123, "Jhonatan", 3.50)
    print(f"Primeiro Print: {acc}")
    acc.deposit(5.50)
    print(f"Segundo Print: {acc}")
    acc.withdraw(1.50)
    print(f"Terceiro Print: {acc}")
    
b_acc = BusinessAccount(321, "Padaria", 500.0, 2000.0)
print(f"1 BC: {b_acc}")
b_acc.loan(2000.0)
print(f"2 BC: {b_acc}")
