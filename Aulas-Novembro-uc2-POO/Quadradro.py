class Quadrado():
        def __init__(self, tamanhoLado):
            self.tamanhoLado = tamanhoLado
        
        def mostrar_area (self):
            return self.tamanhoLado

        def mudar_valor_lado (self):
            return self.tamanhoLado**2
quadrado1=Quadrado(4)
print(quadrado1.mostrar_area()) 

quadrado2=Quadrado(6)
print(quadrado2.mudar_valor_lado())
