compras = []
resposta=(str(input("dejesa adicionar item : ")))
while resposta=="sim":
    add=(str(input("adicionar item")))
    compras.append(add)
    print(compras)
    resposta=(str(input("dejesa adicionar item : ")))
    if resposta=="sim":
        add2=(str(input("adicionar item")))
        compras.append(add2)
        print(compras)
    else:
        remove=(str(input("remover item")))
        compras.remove(remove)
        print(compras)
