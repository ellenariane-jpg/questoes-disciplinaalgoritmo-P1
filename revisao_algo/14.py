'''
def soma_matrizes(a, b):
    nova_matriz = []

    for i in range(len(a)):
        linha = []     
        for j in range(len(a[i])):
            soma = a[i][j] + b[i][j]
            linha.append(soma)
        nova_matriz.append(linha)
    return nova_matriz
   
a = [[1, 0, 2]]
b = [[5, 5, 5]]
print(soma_matrizes(a,b))

def soma_matrizes(c, d):
    nova_matriz = []

    for i in range(len(c)):
        linha = []
        for j in range(len(c[i])):
            soma = c[i][j] + d[i][j]
            linha.append(soma)
        nova_matriz.append(linha)
    return nova_matriz

c = [[2, 4, 6],
     [1, 3, 5]]

d = [[10, 20, 30],
     [40, 50, 60]]

print(soma_matrizes(c,d))
'''
def soma_matrizes(e, f):
    nova_matriz = []
    for i in range(len(e)):
        linha = []
        for j in range(len(e[i])):
            soma = e[i][j] +f[i][j]
            linha.append(soma)
        nova_matriz.append(linha)
    return nova_matriz

e = [[10, 20],
     [30, 40],
     [50, 60]]

f = [[1, 2],
     [3, 4],
     [5, 6]]
print(soma_matrizes(e,f))