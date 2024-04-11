import csv
# Pandas tem quase 200Mb, então usa o próprio da biblioteca se for somente para ler


path: str = "exemplo.csv"
arquivo_csv: list=[]

# Com o with, ele abre e fecha o arquivo, não corre o risco de deixar o arq aberto
# é um gerenciador de contexto
with open(path,"r",encoding="utf-8") as arquivo:
    # Criando um objeto para ler o arquivo
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)

