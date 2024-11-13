
# vermelho = int(input("Digite o valor para vermelho (0 ou 1): "))
# amarelo = int(input("Digite o valor para amarelo (0 ou 1): "))
# verde = int(input("Digite o valor para verde (0 ou 1): "))

# semaforo = vermelho, amarelo, verde
# if vermelho == 0 and amarelo == 0 and verde == 0:
#     print("Semáforo desligado")

# elif vermelho == 1 and amarelo == 0 and verde ==0:
#     print("Vermelho ON")
#     print(" Status: ", vermelho, amarelo, verde)

# elif vermelho == 0 and amarelo == 1 and verde ==0:
#     print("Amarelo ON")
#     print(" Status: ", vermelho, amarelo, verde)

# elif vermelho == 0 and amarelo == 0 and verde == 1:
#     print("Verde ON")
#     print(" Status: ", vermelho, amarelo, verde)
# else:
#     print("Valor inválido")

for a in range(1,11):
    for b in range(1,11):
        print( a, "x", b , "=", a*b)