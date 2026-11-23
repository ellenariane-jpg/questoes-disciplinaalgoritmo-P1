temperaturas = [25,27,26,30,31,29,33]
nova_lista = []
for i in range(len(temperaturas)):
    if temperaturas[i] > temperaturas[i -1]:
        nova_lista.append(i)
print(nova_lista)
