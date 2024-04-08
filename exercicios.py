# Crie um dict para armazenar informações de um livro, incluindo título, autor e anor de publicação. Imprima cada informação
#%%
from typing import Dict, Any
# %%
livro: Dict[str,Any] = {
    "título":"Eu, robô",
    "Autor":"Isaac Asimov",
    "Ano": 1965
}

# %%
lista = (i for i in livro.items())
print(lista)


