
# Exemplo 01:

preço_estimado = 26

if preço_estimado > 25:
    raise ValueError("O preço estimado não pode ser maior que 25")

# Exemplo 02:

scores = [1000, 500, 250, 300, 750, 1100]

if min(scores) < 0 or max(scores) > 1000:
    raise ValueError("Todos os scores devem estar entre 0 e 1000")