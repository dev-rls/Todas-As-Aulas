#Python - Listas
#Uma lista(list) em python é uma sequência ou coleção ordenada de valores.
#Cada valor na lista é identificado por um indice. Os valores que formam uma lista são elementos ou itens.
#Listas são similares a strings, que são uma sequência de caracteres, no entanto, diferentemente de strings, os itens de uima lista podem ser de tipos diferentes.
x="Raquel"
y=["Raquel", 15, 20, 23]

#Existem várias maneiras de ser criar uma nova lista. A maneira mais simples é envolver os elementos da lista por [].
#O primeiro exemplo é uma lista de quatro inteiros. O segundo é uma lista de três strings. Como dissemos anteriormente, os elementos de uma lista não precisam ser do mesmo tipo.
lista1 = [10, 20, 40]
lista2 =["spam", "bungee", "swallow"]
print(lista1, lista2)

#sublist: 
lista1= ["oi", 2.0, 5, [10,20]]
print (lista1)

#Da mesma forma que ocorre com strings, a função len retorna o comprimento de uma lista(o nº de elementos na lista)
#
lista1= ["oi", 2.0, 5, [10,20]]
print (len(lista1))

#Acessando elementos
a= "Raquel"
print(a[3])

numeros= [17, 123,87,34,66,8398,44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-1])
#O que é impresso pelo trecho de código a segir?  
uma_lista = [3,67,"gato", [56,57, "cachorro"], [], 3.14, False]
print(uma_lista[2])
#Resultado: gato

#umalista [3][2][0]

frutas = ["maça", "laranja", "banana", "cereja" ]

print("maça" in frutas) # true
print("pera" in frutas) # false

frutas = ["maça", "laranja", "banana", "cereja" ]
print([1,2]+[3,4])  # [1,2,3,4]
print(frutas + [6,7,8,9]) # ['maça', 'laranja', 'banana', 'cereja', 6, 7, 8, 9]

print([]*4) # []
print([1,2,["ola", "adeus"]]*2) # [1, 2, ['ola', 'adeus'], 1, 2, ['ola', 'adeus']]

# Toda vez que for lista nunca vai somar, sempre que estiver entre [] é lista.
#O que é impresso pelo trecho de código a seguir?
uma_lista= [1,3,5]

# max(), min(), sum()
a= [1,2,3,4,5,6,7,8,9]
print(a)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(max(a)) # 9
print(min(a)) # 1
print(sum(a)) # 45

a= ["A", "B", "C"]
print(max(a)) # C

#Fatias de listas
a= [1,2,3,4,5]
print(a[0:4])

#0=a 1=b 2=c 3=d 4=e 5=f
uma_lista = ['a', 'b', 'c', 'd', 'e','f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[0:6])

# ['b', 'c']
# ['a', 'b', 'c', 'd']
# ['d', 'e', 'f']
# ['a', 'b', 'c', 'd', 'e', 'f']

# 01- faça um programa que receba um vetor  de 5 números inteiros e mostre-os. 
# Mostre o maior deles;
# mostre o menor deles; 
# mostre a quantidade de numeros; 
# some os numeros;

uma_lista = [1,2,3,4,5]
print(a)   
print(max(a)) 
print(min(a)) 
print(sum(a)) 

 # Crie a seguinte lista: Lista = [1,2,1,5,6,3,1]. Mostre quantas vezes o número 1 apareceu.
lista = [1,2,1,5,6,4,3,1]
print(lista)
print(lista.count(1))
