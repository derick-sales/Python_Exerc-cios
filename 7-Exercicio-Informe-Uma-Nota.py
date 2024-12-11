nota = int(input("Informe uma nota"))
while True:
  if nota >= 0 and nota <= 10:
    break
  else:
   print("nota invalida")
   nota = int(input("informe uma nota"))