compras = ["pão","cafe","leite"]
print(compras)

#pode ser removido pelo nome do prduto ou pelo indice
#compras.remove("cafe")
compras.remove(compras[0])
print(compras)

#append acrescenta um item no final da lista, só pode adicionar um por vez
compras.append("açucar")
print(compras)
#é preciso criar uma lista nova para receeber os elementos ordenados da lista antiga
compras_ordenada = sorted(compras)
print(compras_ordenada)
#o nome panela é um identificado dos itens dentro da lista, esses itens podem receber qualquer tipo de nome
for panela in compras:
    print("-", panela)