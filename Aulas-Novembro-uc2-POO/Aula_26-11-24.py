# class encapsulamento():
#     def __init__(self, num1, num2):
#         self.__num1 = num1
#         self.__num2 = num2

#     def adicionar(self):
#         return self.__num1+self.__num2
    
# calc=encapsulamento(20,10)
# print(calc.adicionar())
# calc.__num1

'''O mesmo ocorre no encapsulamento de métodos, * O método __adicionar da linha 22, está disponível apenas no contexto da classe, fora dela ao
chamar o método__adicionar da classe na linha 30, resulta em um erro, pois o método está encapusulado dentro da classe.'''
class encapsulamento():
    def caculadora(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1,num2)
        else:
            print("Operação Inválida")
    
    def __adicionar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        return self.num1 + self.num2

classe = encapsulamento()
result = classe.caculadora('+', 20,10)
print(result)
classe.__adicionar(10,20)

# Classes
'''Em Python, a palavra  reservada __init__ serve para inicialização de classes, como abaixo:'''
class Conta:
    def __init__(self, numero, cpf, nome_titular, saldo):
      self.numero = numero
      self.cpf = cpf
      self.nome_titular = nome_titular
      self.saldo = saldo
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo-= valor
'''No exemplo anterior, adicionamos mais um método sacar(self, valor), onde subtraímos o valor, passado como paramentro, do saldo do cliente

from "nome do arquivo" import "nome da classe"
c1 = Conta(1,1, "Joao",0)
c1.depositar(300)
c1.sacar(100)

* Pode ser adicionado um método extrato para avaliar os valores atuais da conta corrente, ou seja, o estado atual do objeto. Por exemplo, a
conta tinha saldo de 300 reais após o primeiro depósito. Após a chamada de sacar (100), 0 saldo da conta será 200 reais.'''

class Conta:
    def __init__(self, numero, cpf, nome_titular, saldo=0):
      self.numero = numero
      self.cpf = cpf
      self.nome_titular = nome_titular
      self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo-= valor

    def gerar_extrato(self):
        print(f"numero: {self.numero}\n Nome:
              {self.nome_titular}\n cpf:{self.cpf}\nsaldo: {self.saldo}")
'''POO - Pilares

A OOP (Object Oriented Programming -- Programação Orientada a Objetos) pode ser definida por quatro pilares principais, sendo eles herança, encapsulamento, abstração e
polimorfismo.

Encapsulamento
○ conceito de encapsulamento consiste na separação dos aspectos externos (operações) de um objeto acessíveis a outros objetos, além de seus detalhes internos de
implementação, que ficam ocultos dos demais objetos. Algumas vezes, é conhecido como ○ princípio do ocultamento de informação, pois permite que umaclasse encapsule
atributos e comportamentos, ocultando os detalhes da implementação.

Herança
Na orientação a objetos, a herança é um mecanismo por meio do qual classes compartilham atributos e comportamentos, formando uma hierarquia. 
Uma classe herdeira recebe as características de outra classe para reimplementá-las ou especializar de uma maneira diferente da classe pai.
 
A herança permite capturar similaridades entre classes, dispondo-as em hierarquias. As similaridades incluem atributos e operações sobre as classes.
                           ANIMAL
              MAMÍFERO _____|________AVE
               |      |             |    
        CACHORRO     HOMEM        BEIJA-FLOR      
        
Herança
 
class carro:
def__init_(self, n_rodas:int):
self.n_rodas = n_rodas
 
 
def barulho(self):
print("Rammmm")
 
class veiculos(carro):
def _init_(self, n_rodas: int, cor: str):
super()_init_(n_rodas)
self.cor = cor
 
Uma classe pode herdar a definição de outra classe:- Permite uso ou extensão de métodos e atributos previamente definidos em outra
classe - Nova classe
Subclasse - Original
Classe pai, ancestral ou superclasse
- Permite herança múltipla
 
Suponha que a classe ClasseB herda de ClasseA. Um objeto da ClasseB também é um objeto da CasseA Alterar m3() basta modificar a ClasseA
 ClasseA
 +m3()
 +m4()
   ^
   |
ClasseB
+m1()
+m2()
'''
    
