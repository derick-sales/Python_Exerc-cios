salario = int(input("Digite seu salario"))
if salario <= 350:
    salario = salario * 1.15
elif salario > 350 and salario < 600 :
    salario = salario * 1.10
else:
    salario = salario * 1.05
print("este e seu novo salario "+ str(salario))
salario = int(input("Digite seu salario"))
salario = salario * 2.5
print(salario)

salario = int(input("digite seu salario"))
decimo = int(input("digite os meses de trabalho"))
salario = salario * decimo / 12
print("este e seu novo decimo "+ str(salario))
sair = "" 
