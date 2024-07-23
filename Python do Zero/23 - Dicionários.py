# Dicionários:

capitals = {"USA": "Washington DC", 
"Brasil": "Brasilia",
"Canada": "Toronto",
"Argentina": "Buenos Aries"}


capitals.update({"Germany":"Berlin"})  # Adiciona um novo termo ao dicionário

capitals.pop("Argentina")  # Remove um termo do dicionário.

capitals.clear()  # Remove todos os termos do dicionário.

# print(capitals["Argentina"])

# print(capitals.get("Germany"))  # Nesse método, termos que não estão no dicionário serão classificados como "None".

# print(capitals.keys())  # Mostra as palavras chaves do dicionário.

# print(capitals.values())  # Mostra as palavras associadas às palavras cahves.

# print(capitals.items())  # Exibe rodo o dicionario.

for key,value in capitals.items():
    print(key, value)  # Exibe o dicionário de maneira mais bunitinha.

    
