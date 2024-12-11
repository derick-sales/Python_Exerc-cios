qtd_pessoas = int(input(" Digite a quantidade de pessoas: "))

qtd_masculino = 0 
qtd_feminino = 0 

for pessoa in range(qtd_pessoas):
  sexo = input("Informe o sexo: M ou F").upper()

  if sexo == "M" or sexo == "m":
    qtd_masculino +=1
    print(qtd_masculino)
  else:
    qtd_feminino +=1
    print(qtd_feminino)