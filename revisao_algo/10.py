
def eh_polindromo(palavra):
    pilha = []
    for letra in palavra:
        pilha.append(letra)
    for letra in palavra:
        if letra != pilha.pop():
            return False
    return True
print(eh_polindromo('arara'))
print(eh_polindromo('radar'))
print(eh_polindromo('python'))
