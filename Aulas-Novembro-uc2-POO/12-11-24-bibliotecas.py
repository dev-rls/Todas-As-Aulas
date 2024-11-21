''' Import math
Após chamar a biblioteca poderá utilizar suas funções: 

math.ceil(x)

Retorna o limite máximo de x, o menor inteiro maior ou igual que x.

Se x não é um float, deve retornar um valor do tipo integral.'''
# import math

# x=3.5
# print(math.ceil(x))

'''math.fabs(x)
Retorna o valor absoluto de x.
import math
x=3.5
print(math.fabs(x)) '''
 
'''import math

z = -3

print(math.fabs(z))

import math

math.factorial(z)
z=3
print(math.factorial(z))'''

#math.floor = arredonda para menor

'''import math
y=3.5
print(math.floor(y))'''

'''#math.isqrt(n): Retorna a raiz quadrada inteira do inteiro não negativo n. Este é o piso da raiz quadrada exata de n.
SQRT retorna float '''
# import math
# x=81
# print(math.sqrt(x))

'''math.pow(x,y)
Retorna x elevado a potencia de y.
'''
# import math
# x =2
# y =10
# print(math.pow(x,y))

'''O datetime fornece classes para manipulação de datas e horas.
Embora a aritmética de data e hora seja suportada, o foco da implementação está na extração eficiente de atributos para formatção de saída.'''
# import datetime
# print(datetime.date.today())

'''Formatando datas em strings usando o método strftime().
* O metodo strftime(), o que toma como parametro a formatação que queremos  em nossa string de data e, desse modo, nos dá maior liberdade
para decidimos como queremos exibir a data.'''

# import datetime
# print(datetime.date.today().strftime(%d/%m/%Y))

# import time
# a=0
# x=time.perf_count()
# while a<10000:
#     print(a)
#     a+=1
# y =time.perf_counter()
# print(y-x)