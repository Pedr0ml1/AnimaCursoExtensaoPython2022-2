nome = input("informe seu nome: ")
nota = float(input("digite sua nota: "))
if nota == 10 :
  print(f"{nome}, você é brabo")
elif(nota >= 6 and nota < 10):
  print(f"{nome}, nada mal, mas poderia ser melhor")
else:
  print("BURRO!")