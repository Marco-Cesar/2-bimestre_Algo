import time

#variaveis globais
ligado = False 
tempo = 0
potencia = 0

def ligar(novo_tempo, novo_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo = novo_tempo
        potencia = novo_potencia
        print(f'microondas ligador por {tempo} segundos na potência {potencia}')
        iniciar_cronometro(tempo)
        desligar()
    else:
        print('o microondas ja esta ligado')

def desligar():
    global ligado
    if ligado:
        ligado = False
        print(' microondas esta desligado')
    else:
        print('microondas ja esta desligado')

def status():
    if ligado:
        print(f'tempo: {tempo} segundos \n potecia: {potencia}')
    else:
        print(f"desligado")

def iniciar_cronometro(segundos):
    while segundos>0:
        print(f"tempo restante: {segundos} segundos",end="\r")
        time.sleep(1)
        segundos -= 1 # segundos = segundos + 1
    print("\n tempo esgotado")

#predefinoções do microondas

def pipoca():
    ligar(30, 100)

#rodar a função

pipoca()    