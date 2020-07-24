def gen_primos():
    """Generador de numeros primos"""
    contador = 1
    lista_primos =[]
    #comienza una secuencia infinita
    while True:
        es_primo = True
        contador += 1
        if len (lista_primos) > 0 :
            for primo in lista_primos:
                if contador % primo == 0 :
                    es_primo = False
                    break
        if es_primo:
            lista_primos.append (contador)
            yield contador

generador = gen_primos()
generador.__next__()
print(type(generador))
print(next(generador))
print(next(generador))
print(next(generador))