lista = [1,2,3,4]
pilha = []
def inverter(lista):
    for elemento in lista:
        pilha.append(elemento)
    nova_lista = []
    while len(pilha) > 0:
        nova_lista.append(pilha.pop())
    return nova_lista
print(inverter(lista))