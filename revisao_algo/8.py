pares = 0
impares = 0
maior = 0
while True:
    numero = int(input('Número inteiro positivo (0 para encerrar): '))
    if numero == 0:
        break
    elif numero < 0:
        continue
    if numero % 2 == 0:
        pares += 1
    elif numero % 2 == 1:
        impares += 1
    if numero > maior:
        maior = numero
print(f'Pares: {pares}')
print(f'Ìmpares: {impares}')
print(f'Maior número: {maior}')