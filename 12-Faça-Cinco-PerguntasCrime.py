questionario_1 = input("telefonou para a vitima?")
questionario_2 = input("esteve no local do crime")
questionario_3 = input("mora perto da vitima")
questionario_4 = input("devia para a vitima")
questionario_5 = input("Já trabalhou com a vitima")
contador = 0
if questionario_1 == "sim":
   contador += 1
if questionario_2 == "sim":
   contador += 1
if questionario_3 == "sim":
   contador += 1
if questionario_4 == "sim":
   contador += 1
if questionario_5 == "sim":
   contador += 1
if contador == 3 or contador == 4 :
  print("Cumplice do crime")
elif contador == 5:
  print("Assasino")
elif contador == 2:
  print("suspeito")
else:
  print("inocente")