class Retangulo():
    def __init__(self,comprimento, largura):
        self.comprimento=comprimento
        self.largura=largura
   
    def Comp (self, comprimento, largura):
        self.comprimento= float(input("Insira o valor do comprimento: "))
        self.largura= float(input("Insira o valor da largura: "))
        return print(self.comprimento, self.largura)
    def Area (self):
        return self.comprimento*self.largura
    def Larg (self):
        return ((self.comprimento*2)+(self.largura*2))
   
retangulo= Retangulo (0,0)
retangulo.Comp (0,0)
print("A área do retângulo é:",retangulo.Area())
print("A largura do retângulo é:",retangulo.Larg())