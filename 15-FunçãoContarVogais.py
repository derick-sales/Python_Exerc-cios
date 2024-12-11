lista_vogais = ["a", "e", "i", "o", "u"]

def contar_vogais(texto):
    quantidade_vogais = 0 
    for letra in texto:
        if letra in lista_vogais:
            quantidade_vogais += 1
    print(quantidade_vogais)
        

contar_vogais("aaaa")