import os

# Definindo o nome atual e o novo nome do arquivo
nome_atual = 'from time import sleep.py'
novo_nome = 'projectpython.py'

# Renomeando o arquivo
os.rename(nome_atual, novo_nome)

print(f"Arquivo renomeado de {nome_atual} para {novo_nome} com sucesso!")