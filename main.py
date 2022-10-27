#Meu primeiro projeto python
print("Olá mundo")
nome = "Pedro Munhoz"
idade = 21
print("Meu nome é "+nome)
print("minha idade é "+str(idade)+" anos")
nome = input("Qual é o seu nome? ")
input(f"Boa noite, {nome}")
idade = int(input("Quantos anos você tem? "))
if idade >= 18 : 
  print("Já pode ser preso kkkkkk")
else:
  print("Vai dormi!!")
sexo = input( "informe o seu sexo M=Masculino, F=Feminino: " )
if idade >= 18 and sexo == "M":
  print("presta/prestou serviço militar obrigatório? ")