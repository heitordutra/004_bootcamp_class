# Dicionário possui estrutura chave-valor
# lista é um elemento
import json
lista = ["Sapato", 39, 10.38, True]

produto_1 = {
    "nome":"Sapato",
    "quantidade":39,
    "preco":10.38,
    "disponibilidade":True
}

produto_2 = {
    "nome":"Televisao",
    "quantidade":10,
    "preco":70.38,
    "disponibilidade":True
}

carrinho: list=[]

carrinho.append(produto_1)
carrinho.append(produto_2)

print(carrinho) #lista de dicionário
print()
carrinho_json = json.dumps(carrinho)
print(carrinho_json)