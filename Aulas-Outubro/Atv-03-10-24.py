 # 01 - Crie a seguinte lista: Lista = [1,2,1,5,6,4,3,1]. Mostre quantas vezes o número 1 apareceu.
# lista = [1,2,1,5,6,4,3,1]
# print(lista)
# print(lista.count(1))

# # 02 - Faça um Programa  que receba um vetor de 5 frutas mostre-os. Depois, substitua o segundo elemento do vetor por laranja.
# frutas = ["goiaba", "maça", "pitaya", "melão", "uva"]
# print(frutas)
# frutas[-4] = "laranja" # ou 1
# print(frutas)

# # 03 - # Faça um programa que contenha a temperatura média de cada mês do ano e armazene-as em lista. Após isto, calcule a média anual das temperaturas, mostre a maior
# # e a menor. imprimir em ordem crescente e decrescente. Não utilizar as mesmas tempertauras.

# lista_meses = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
# lista_meses.extend([])
# print(lista_meses)

jan = ["jan", 25, 17]
fev = ["fev", 22, 20]
mar = ["mar", 18, 32]
abr = ["abr", 16, 42]
mai = ["mai", 26, 28]
jun = ["jun", 29, 31]
jul = ["jul", 23, 39]
ago = ["ago", 27, 35]
set = ["set", 21, 33]
out = ["out", 19, 38]
nov = ["nov", 10, 15]
dez = ["dez", 17, 24]

temp1 = [10,20,28,40,33,40,37,38,32,27,17,35]
temp2 = [18,21,25,42,34,30,36,39,31,25,15,23]

media_anual = (sum(temp1)) + sum (temp2)/(len(temp1) + len(temp2))

maior_temp = max (max(temp1) + max(temp2))
menor_temp = min (min(temp1) + min(temp2))

lista_temperaturas = temp1 + temp2
crescente = lista_temperaturas.sort(lista_temperaturas)
decrescente = lista_temperaturas.sort(lista_temperaturas,reverse=True)



# Faça um programa que contenha duas temperaturas por mês, uma em cada lista de todos os meses do ano. Após isto, calcule a média anual das temperaturas, mostre a maior
# e a menor. imprimir em ordem crescente e decrescente. Não utilizar as mesmas tempertauras.

# jan = ["jan", 25, 17]
# fev = ["fev", 22, 20]
# mar = ["mar", 18, 32]
# abr = ["abr", 16, 42]
# mai = ["mai", 26, 28]
# jun = ["jun", 29, 31]
# jul = ["jul", 23, 39]
# ago = ["ago", 27, 35]
# set = ["set", 21, 33]
# out = ["out", 19, 38]
# nov = ["nov", 10, 15]
# dez = ["dez", 17, 24]

#lista.sort()

# temp = [jan, fev, mar, abr, mai, jun, jul, ago]
# print(temp)   
# print(max(temp)) 
# print(min(temp)) 
# print(sum(temp))

