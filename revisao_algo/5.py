total = 0
carros = 0

while True:
    horas = int(input('Horas de permanencia (0 para encerrar): ' ))
    if horas == 0:
        break
    elif horas < 0 or horas > 24:
        print('Valor Inválido')
    else:
        total += horas * 5
        carros += 1
print(f'Quantidade de carros: {carros}')
print(f'Total Arrecadado: R${total}')
if total > 200:
    print('Dia bom!')