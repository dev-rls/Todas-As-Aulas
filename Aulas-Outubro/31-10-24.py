#Maratona
c1 = 0
c2 = 0
c3 = 0
c4 = 0
nulos = 0
brancos = 0

while True:
   voto = int(input("Digite o número do seu canditado (0 para finalizar): "))
   if voto == 0:
      print("Sessão finalizada")
      break
   if voto == 1:
      c1 = c1 +1
   elif voto == 2:
      c2 = c2 +1
   elif voto == 3:
      c3 = c3 +1
   elif voto == 4:
      c4 = c4 +1
   elif voto == 6:
      nulos = nulos +1
   elif voto == 8:
      brancos = brancos +1
   else:
      print("Código inválido! Voto não contabilizado")

print("Resultado da Eleição")
print("\nVotos canditado A: ", c1)
print("\nVotos canditado B: ", c2)
print("\nVotos canditado C: ", c3)
print("\nVotos canditado D: ", c4)
print("\nVotos Nulos: ", nulos)
print("\nVotos Brancos: ", brancos)
