# tradutor = {}
# tradutor ["pineapple"] = "abacaxi"
# tradutor ["apple"] = "maça"
# tradutor ["orange"] = "laranja"
# print(type(tradutor))
# print(tradutor)


# tradutor = {}
# tradutor1 = {"pineapple": "abacaxi", "apple":"maça", "orange": "laranja"}
# print(type(tradutor1))
# print(tradutor1)

#  Python - Dicionários - Pesquisando
#  O exemplo mostra como usar uma chave para pesquisar o valor correspondente.

# tradutor1={}
# tradutor1 = {"pineapple": "abacaxi",
# "aple": "maça", "orange": "laranja"}

# print(tradutor1["apple"])


# O exemplo mostra como usar uma chave para pesquisar o valor correspondente
# tradutor1 = {}
# tradutor1 = {"pineapple": "abacaxi", "apple":"maça", "orange": "laranja"}
# print(tradutor1)
# del(tradutor1 ["apple"])
# print(tradutor1)

# Python - Dicionários - Removendo uma chave-valor

# print(tradutor1.pop('banana','Fruta não encontrado'))

# Python - Dicionários - Removendo uma chave-valor | clear() - Remove todos os elementos do dicinário

# traduto1.clear()

# tradutor1 = {}
# tradutor1 = {"pineapple": "abacaxi", "apple":"maça", "orange": "laranja"}
# print("pineapple" in tradutor1)

# # O comando in verifica apenas as chaves do dicionário, não os valores. Para obtermos valores, podemos usar o método values():
# print('laranja' in a.values())

# # Imprimindo os valores do dicinário 
# print(tradutor1())

# tradutor1 = {}
# tradutor1 = {"pineapple": "abacaxi", "apple":"maça", "orange": "laranja"}
# print(tradutor1)
# tradutor1["apple" ]= "goiaba" 
# print(tradutor1)

# É possível criar um dicionário dentro de uma chave de um dicionário:

# dados = {'Crossfox':{'km': 35000, 'ano' : 2005}, 'DS5':{'km':17000,'ano':2015},
#          'Fusca':{'km':130000,'ano':1979}, 'Jetta':{'km':56000,'ano':2011},
#          'Passat':{'km':62000, 'ano':1999}
# }
# print(dados)

# print(dados.get('Gol', 'veículo não encontrado')) #Os dicionários possuem um metodo especifico para busca de valores, o get(), no qual podemos passar como 
# #parametros a chave  que queremos e um valor padrão para retornar caso essa chave não seja encontrada

# Atividade 01 - Faça um dicionário com as 5 pessoas mais perto  de você, tendo o nome chave e a idade como valor.

# pessoas = {'Jamily':{'idade': 21}, 'Eduarda':{'idade':23},
#           'Dayane':{'idade':31}, 'Abel':{'idade':16},
#           'Alexandre':{'idade':33}
# }
# print(pessoas)
# for i in dic:
#     print( i, "Jamily-21": dic[i])

# try: # Podemos utilizar o bloco Try para tratar essa exceção:

#     a = int (input(" Digite uma palavra: "))
# except: # O bloco try erro caso seja digitada uma letra, e o except trará uma ação caso ocorra erro.
#     print("Digite apenas números: ") 

# # Multiplas Exceções:
# try:
#     a = int (input(" Digite uma palavra: "))
# except ValueError:
#     print("Digite apenas números")
# except:
#     print("Erro desconhecido")

# Finally: executa independente de erros:

# try:
#     a = int (input(" Digite uma palavra: "))
# except ValueError:
#     print("Digite apenas números")
# except:
#     print("Erro desconhecido")
# finally:
#     print("Final algoritmo")

# Tratamento de Erros:

# 4 + spam*3 - NameError
# While True print('Hello world') - SytanxError
# 10*(1/0) - ZeroDivisionError
# '2'+ 2 - TypeError

# Atividade 02 - Calculadora - Elabore uma calculadora com todas as operações básicas. Utilize Try e Except.

while True:

    try:
        calculadora = int (input("1.Multiplicação\n 2.Divisão\n 3.Adição\n 4.Subtração\n 5.Sair\nDigite a operação desejeda: "))
        if calculadora == 1:
            num1 = float(input("Digite o valor 1: "))
            num2 = float(input("Digite o valor 2: "))
            num3= num1*num2
            print(num3)

        elif calculadora == 2:
            num1 = float(input("Digite o valor 1: "))
            num2 = float(input("Digite o valor 2: "))
            num3= num1/num2
            print(num3)
        elif calculadora == 3:
            num1 = float(input("Digite o valor 1: "))
            num2 = float(input("Digite o valor 2: "))
            num3= num1+num2
            print(num3)

        elif calculadora == 4:
            num1 = float(input("Digite o valor 1: "))
            num2 = float(input("Digite o valor 2: "))
            num3= num1-num2
            print(num3)
        elif calculadora == 5:
            print("Saindo")
            break
    except ValueError:
        print("Digite apenas números")
    except:
        print("Erro desconhecido")