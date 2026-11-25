def somar_colunas(matriz):
    coluna = []
    for j in range(len(matriz[0])):
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][j]
        coluna.append(soma)
    return coluna

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]
print(somar_colunas(matriz))