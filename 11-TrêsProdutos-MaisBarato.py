produto_1 = int(input("digite o preço do produto"))
produto_2 = int(input("digite o preço do produto"))
produto_3 = int(input("digite o preço do produto"))

if produto_1 < produto_2 and produto_1 < produto_3:
  print("voce deve comprar esse", produto_1)
elif produto_2 < produto_1 and produto_2 < produto_3:
  print("voce deve comprar esse", produto_2)
else:
  print("voce deve comprar esse", produto_3)