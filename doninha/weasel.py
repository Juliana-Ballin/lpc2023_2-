import random

# Taxa de mutação (chance de uma letra ser alterada)
CHANCE = 5
# Conjunto de letras possíveis, incluindo um espaço em branco
letras = 'abcdefghijk lmnopqrstuvwxyz'
# String inicial gerada aleatoriamente
frase = ''
# Frase que estamos tentando gerar (o alvo)
WEASEL = 'methinks it is like a weasel'
# Pontuação inicial da frase gerada em relação à frase alvo
score = 0
# Contador de gerações
geracao = 0

# Geração aleatória da frase inicial
for i in range(28):
    frase += letras[random.randint(0, 26)]
# Imprime a frase inicial
print(frase)


def update():
    global frase, WEASEL, score, CHANCE
    # Loop para gerar 100 variações da frase atual
    for i in range(100):
        novo_score = 0
        # Cria uma cópia da frase atual como uma lista
        nova_frase = list(frase)
        # Loop para percorrer cada posição na frase
        for c in range(28):
            # Verifica se a letra será alterada com base na chance
            if random.randint(0, 99) < CHANCE:
                # Se sim, substitui a letra na posição atual
                nova_frase[c] = letras[random.randint(0, 26)]
        # Loop para calcular a pontuação da nova frase gerada
        for j in range(28):
            if nova_frase[j] == list(WEASEL)[j]:
                novo_score += 1
        # Se a pontuação da nova frase for maior que a pontuação atual
        if novo_score > score:
            # Atualiza a pontuação e a frase atual
            score = novo_score
            frase = ''
            for i in range(28):
                frase += nova_frase[i]


# Loop até que a pontuação atinja o valor máximo (28, que é o comprimento da frase alvo)
while score != 28:
    # Chama a função para gerar novas variações da frase
    update()
    # Incrementa o contador de gerações
    geracao += 1
    # Imprime a geração atual e a frase correspondente
    print(f'Geração {geracao}: ' + frase)
    
# Imprime o número total de tentativas necessárias
print(f'\nConcluído em {geracao} gerações!')
