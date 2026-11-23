preco = [12.0,45.0,8.5,60.0,30.0,5.0]
novo_preco = []
for i in range(len(preco)):
    produto = preco[i]
    if produto >= 30.0:
        p = (produto * 10) / 100
        d = produto - p
        novo_preco.append(d)
    elif i % 2 == 1:
        novo_preco.append(produto + 2)
    else:
        novo_preco.append(produto)
print(novo_preco)