numeros = [7, 12, 5, 18, 9, 20, 3, 14]
pares = []
impares = []
for i in range(len(numeros)):
    if i % 2 == 0:
        pares.append(numeros[i])
    elif i % 2 ==1:
        impares.append(numeros[i])
print(pares)
print(impares)