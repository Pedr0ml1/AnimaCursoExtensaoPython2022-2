preco = 1999.99
imposto = preco * 0.05
print(preco)
print(imposto)
def calcular_imposto(preco_produto):
  imposto = preco_produto * 0.05
  return imposto
print(preco)
print(preco_produto)
valores = [1.99, 25.50, 35.00, 10.00]
print(f"O imposto de {valores} é {calcular_imposto(valor)}")