lista_de_numeros: list = [40,50,60,70,0,-408593,1,50]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(numeros)):
        for j in range(i+1,len(numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = nova_lista_de_numeros[j], nova_lista_de_numeros[i]
    return nova_lista_de_numeros

nova_lista = ordenar_lista_de_numeros(lista_de_numeros)

print(nova_lista)

# Se quiser usar essa função em outro arquivo, pode usar from <nome do arquivo> import <nome da funcao>