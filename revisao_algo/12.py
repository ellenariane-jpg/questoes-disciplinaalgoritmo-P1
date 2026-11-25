'''
fila = []
fila.append('Ellen')
fila.append('Ana')
fila.append('maria')
print(fila)
remova = fila.pop(0)
print(fila)
remova1 = fila.pop(0)
print(fila)
'''
def intercalar(fila1, fila2):
    f1 = fila1.copy()
    f2 = fila2.copy()
    resultado = []
    while len(f1) > 0 and len(f2) > 0:
        resultado.append(f1.pop(0))
        resultado.append(f2.pop(0))
    resultado.extend(f1)
    resultado.extend(f2)
    return resultado
print(intercalar(['ana', 'carla', 'elisa'], ['bruno', 'diego'])) 
