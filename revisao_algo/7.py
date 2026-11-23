total = 0
maior_que_7 = 0
quantidade = 0
while True:
    notas = float(input('Nota (-1 para encerrar): '))
    if notas == -1:
        #print('Nenhuma nota registrada')
        break
    elif notas <0 or notas > 10:
        print('Nota Inválida.')
    else: 
        total += notas
        quantidade += 1
        if notas > 7:
            maior_que_7 += 1
if quantidade > 0:
    media = total / quantidade
    print(f'Média: {media:.2f}')
    print(f'Notas maiores que 7: {maior_que_7}') 