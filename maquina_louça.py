import time

ligado = False 
tempo = 0
grau = 0

def ligar(novo_tempo, novo_grau):
    global ligado, tempo, grau
    if not ligado:
        ligado = True
        tempo = novo_tempo
        grau = novo_grau
        print(f'maquina de louça ligador por {tempo} segundos no grau {grau}')
        iniciar_cronometro(tempo)
        desligar()
    else:
        print('o maquina de louça ja esta ligado')

def desligar():
    global ligado
    if ligado:
        ligado = False
        print('maquina de louça esta desligado')
    else:
        print('maquina de louça ja esta desligado')

def status():
    if ligado:
        print(f'tempo: {tempo} segundos \n grau: {grau}')
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos",end="\r")
        time.sleep(1)
        segundos -= 1 
    print("\n tempo esgotado")

def vidro():
    ligar(120, 100)

def plastico():
    ligar(60, 21)

def metal():
    ligar(120, 30)

print("escolha 1 - vidro, 2 - plastico, 3 - metal")
escolha=int(input("escolha 1, 2, 3"))
match escolha:
    case 1:
        vidro()
    case 2:
        plastico()
    case 3:
        metal()