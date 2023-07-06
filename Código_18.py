# Deletar um arquivo:


import os

# Obtém o diretório de trabalho atual
diretorio_atual = os.getcwd()

# Constrói o caminho completo do arquivo
caminho_arquivo = os.path.join(diretorio_atual, "Bunda.py")

# Verifica se o arquivo existe e o exclui
if os.path.exists(caminho_arquivo):
    os.remove(caminho_arquivo)
    print(f"O arquivo {caminho_arquivo} foi excluído com sucesso.")
else:
    print(f"O arquivo {caminho_arquivo} não existe.")

