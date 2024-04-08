# %%
# 1 Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista = list(range(1,11))

for i in lista:
    print(i**2)

# %%
# 2 Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".

lista: list = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)
# %%
# 3 Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
dicionario: dict = {"titulo":"Eu, robo",
                    "autor": "Isaac Asimov",
                    "ano": 1965}
for i in dicionario.keys():
    print(f"{i}: {dicionario[i]}")
# %%
# 4 Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
import string
alphabet = list(string.ascii_lowercase)
word = input("Write the word: ")
word_letters = [*word]
word_letters.sort()
letters = {}
for i in word_letters:
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1
print(letters)
    



# %%
# 5 Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = 0
for i in lista:
    total += precos[i]
print(total)