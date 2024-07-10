
name = "MonA Sax"

first_name = name[2]  # Oferece a posição do caractere desejado.

first_name = name[0:4]  # Defini o limite de caracteres que irão aparecer no terminal.  Obs: Defini ou não "0" como ponto de partida não faz diferença na linguagem python.

last_name = name[4:8]

funky_name = name[0:8:2]  # Pula caractere dependo da frequência oferecida em número.

reversed_name = name[::-1]


# Define os caracteres a serem removidos
chars_to_remove = "on AS"

# Cria uma nova string filtrando os caracteres
filtered_name = ''.join(c for c in name if c not in chars_to_remove)

print(filtered_name)


