ano_contratacao = 1995
ano_atual = int(input("informe o ano atual"))

anos = ano_atual - ano_contratacao
salario_inicial = 1000
porcentagem = 1.5/100

for a in range(anos):
  porcentagem = porcentagem * 2

salario_final = salario_inicial * (1 + porcentagem)
print(salario_final)
