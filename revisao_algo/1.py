lista = [4,9,15,22,30,7]
nova_lista = []

for indices in range(len(lista)):
    elemento = lista[indices]
    if elemento % 3 == 0:
       resultado = elemento // 3
       nova_lista.append(resultado)
    elif indices % 2 == 0:
        soma = elemento + indices
        nova_lista.append(soma)
print(nova_lista)