# Numpy
'''import numpy as np
array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
    [[10,11,12],[13,14,15],[16,17,18]],[[19,20,
    21],[22,23,24],[25,26,27]]])

print(array_3d)'''

'''import numpy as np

a =np.random.rand(5)
print(a)

import numpy as np
n =np.random.rand(5)

array = np.arange(1,12,2)
print(n)'''

'''Exercicio 01 : Criando e manipulando arrays.
Crie um array de 10 numeros aleatorios entre 0 e 1.
Calcule a soma, média, valor máximo e mínimo desse array.
Reshape o array para uma matriz 2x5.'''
# import numpy as np
# n =np.random.rand(2,5)
# print(n)
# print(np.sum(n))
# print(np.min(n))
# print(np.max(n))
# print(np.mean(n))

'''Exercicio 02
Crie um array com dois números de 0 a 20.
Selecione os elementos pares.
Calcule a média dos elementos ímpares.
'''
# import numpy as np
# n =np.random.rand(0,20)
# print(n)

'''Biblioteca PyDantic'''

# from pydantic import BaseModel
# class Usuario(BaseModel):
#     nome:str
#     idade:int
#     email:str
# usuario=Usuario (nome="João",idade=54,email="joao@exemplo.com")
# print(usuario.nome)
# print(usuario.idade)
# print(usuario.email)

#Exercicio 2
from pydantic import BaseModel
class Usuario(BaseModel):
    nome:str
    sexo:str
    idade:int
usuario=Usuario (nome="Jhon",sexo="Masculino",idade=60)
print(usuario.nome)
print(usuario.sexo)
print(usuario.idade)