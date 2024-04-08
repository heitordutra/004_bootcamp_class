# %%
# 6 Objetivo: Dada uma lista de emails, remover todos os duplicados.
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

# %%
# 7 Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]
idades_filtradas = [i for i in idades if i>18]
print(idades_filtradas)

# %%
# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["idade"])
print(pessoas)

# %%
# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]
media = sum(numeros)/len(numeros)
print(media)

# %%
# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [i for i in valores if i%2==0]
impares = [i for i in valores if i%2==1]

print(pares)
print(impares)

# %%
# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
    ]

for i in produtos:
    if i["id"]==2:
        i["preço"] = 350

print(produtos)

# %%
# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario = {**dicionario1,**dicionario2}
# ou dicionario = dicionario1 | dicionario2

# %%
# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}
estoque_0 = {i for i in estoque if estoque[i]>0}
print(estoque_0)

# %%
# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print(chaves)
print(valores)
# %%
# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

