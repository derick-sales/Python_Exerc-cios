numero_anterior = 1
numero_meio = 1 

proximo_numero = 0 

for i in range(10):
  proximo_numero = numero_anterior + numero_meio 
  numero_anterior = numero_meio 
  numero_meio = proximo_numero
  print(numero_anterior)