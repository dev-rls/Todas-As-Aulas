class Quadrado():
        def __init__(self, tamanhoLado):
            self.tamanhoLado = tamanhoLado
        
        def mostrar_area (self):
            return self.tamanhoLado

        def mudar_valor_lado (self):
            return self.tamanhoLado**2

quadrado1= Quadrado(4)
print(f"A área do quadrado é {quadrado1.tamanhoLado}.")
print("A área é:",quadrado1.mostrar_area()) 

quadrado2 = Quadrado(6)
print(f"O valor do lado do quadrado é {quadrado2.tamanhoLado}.")
print("A área modificada é:",quadrado2.mudar_valor_lado())
