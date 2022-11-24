print("FRUTAS")
frutas = ["morango","laranja","pera"]
frutas.append("manga")
print(len(frutas))
i=0
while(i<4):
  print(frutas[i])
  i = i + 1
for fruta in frutas:
  print(fruta)
#funções
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
preco = 2000
valores = [1.99, 15.90, 2.00, 36.00]
