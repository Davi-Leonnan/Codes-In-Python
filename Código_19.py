# Quiz:

perguntas = [
    {
        'pergunta': 'Qual é a capital do Brasil?',
        'opcoes': ['São Paulo', 'Rio de Janeiro', 'Brasília', 'Salvador'],
        'resposta': 'Brasília'
    },
    {
        'pergunta': 'Qual é o maior planeta do Sistema Solar?',
        'opcoes': ['Júpiter', 'Saturno', 'Vênus', 'Terra'],
        'resposta': 'Júpiter'
    },
    {
        'pergunta': 'Quem pintou a Mona Lisa?',
        'opcoes': ['Michelangelo', 'Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh'],
        'resposta': 'Leonardo da Vinci'
    }
]

pontuacao = 0

for pergunta in perguntas:
    print(pergunta['pergunta'])
    for i, opcao in enumerate(pergunta['opcoes']):
        print(f"{i + 1}. {opcao}")

    resposta = input("Digite o número da opção correta: ")
    resposta = int(resposta) - 1

    if pergunta['opcoes'][resposta] == pergunta['resposta']:
        print("Resposta correta!")
        pontuacao += 1
    else:
        print("Resposta incorreta!")

    print()

print(f"Fim do quiz! Sua pontuação final é: {pontuacao}/{len(perguntas)}")


