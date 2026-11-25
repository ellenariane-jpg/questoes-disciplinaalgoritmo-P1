def  atendidos(clientes, tempo_disponível):
    resultado = []
    for i in clientes:
        if i[1] <= tempo_disponível:
            resultado.append(i[0])
            tempo_disponível -= i[1]
        else:
            break
    return resultado
clientes = [['Ana', 5],['Bruno', 10],['Carla', 3],['Diego', 8]]
print(atendidos(clientes, 20))