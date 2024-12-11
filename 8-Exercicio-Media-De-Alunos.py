turmas = int(input("Digite a quantidade de turmas: "))
contador = 0
soma = 0

while contador < turmas: 
  alunos = int(input("Digite a quantidade de alunos: "))

  if alunos <= 40:
  # contador = contador +1
   contador += 1
  # soma = soma + alunos
   soma += alunos
  else:
    print("Numero de alunos invalido")


media = soma / turmas
print(media)