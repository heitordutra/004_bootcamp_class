produto_1: str = "sapato"
produto_2: str = "camiseta"
produto_3: str = "videogame"

produtos: list=[]

produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.pop() # pop remove a ultima, o remove() voce escolhe qual remover. pop é mais performático

# %%
numeros = []
# extend() adiciona um range, append adiciona um item
numeros.extend(range(0,5))

print(numeros)
