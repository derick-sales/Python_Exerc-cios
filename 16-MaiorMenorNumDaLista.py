def achar_maior_menor(lista):
    maior_valor = 0
    menor_valor = 0

    for num in lista:
        if num > maior_valor:
            maior_valor = num
        
        if num < menor_valor:
            menor_valor = num

    print(maior_valor, menor_valor)

achar_maior_menor([-5, 0, 2, 3, 6, 12])