doacoes = 0
total = 0
while True:
     quantidade = float(input('Quilos doados (0 para encerrar): '))
     if quantidade == 0:
          break
     elif quantidade < 0:
          print('Doação Inválida.')
     else:
          doacoes += 1
          total += quantidade
print(f'Quantidade de doações: {doacoes}')
print(f'Total Arrecadado: {total} kg')
if total >= 50.0:
     print('Meta atingida!')
else:
     print(f'Faltam {50 - total} kg para a meta.') 