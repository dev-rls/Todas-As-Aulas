'''Vamos criar a super classe'''
# class Super:
#     def hello(self):
#         print("Olá, sou a superclasse!")

# teste = Super() #Implementação
# teste.hello()

# Agora o resultado:
# Olá, sou a superclasse!

'''Agora vamos criar outra classe, a Sub, que vai herdar a superclasse e vamos definir nela um método de mesmo nome hello(), mas com um texto diferente: '''

# class Super:
#     def hello(self):
#         print("Olá, sou a superclasse!")
    
# class Sub(Super):
#     def hello(self):
#         print("Olá, sou a subclasse")

# teste = Sub() #Implementação
# teste.hello()

# Agora o resultado:
# Olá, sou a subclasse!

'''Agora vamos criar outra classe, a Subsub, que vai herdar a subclasse e vamos definir nela um método de mesmo nome hello(), mas com um texto diferente: '''
# class Super:
#     def hello(self):
#         print("Olá, sou a superclasse!")
    
# class Sub(Super):
#     def hello(self):
#         print("Olá, sou a subclasse")

# class Subsub(Sub):
#     def hello(self):
#         print("Olá, sou a subsubclasse")

# teste = Subsub() #Implementação
# teste.hello()

# Agora o resultado:
# Olá, sou a subsubclasse!

class Super:
    def printar(self):
        print("teste")
    
class Sub(Super):
    def hello(self):
        print("Olá, sou a subclasse")

class Subsub(Sub):
    def hello(self):
        print("Olá, sou a subsubclasse")

    def printar(self):
        print("teste")

teste = Super()
teste.printar()

