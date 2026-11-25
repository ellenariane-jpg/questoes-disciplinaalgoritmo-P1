def profundidade(expressao):
    pilha = []
    maior =0
    for caractere in expressao:
        if caractere == '(':
            pilha.append(caractere)
            if len(pilha) > maior:
                maior = len(pilha)
        elif caractere == ')':
            pilha.pop()
    return maior
print(profundidade('(a + b) * (c + d)'))
print(profundidade('((a + b) * (c -(d + e)))'))
print(profundidade('a + b'))