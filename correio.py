pacotes=( ("ABC123"), ("XYZ789"), ("DEF456"), ("JKL321"), ("MNO654"), ("PQR987"), ("STU741"))
rastreio=( ("Enviado"), ("Recebido"), ("Em Trânsito"), ("Enviado"), ("Recebido"), ("Em Trânsito"), ("Enviado"))
print("os Enviados", rastreio.count("Enviado"))
print("os Recebidos", rastreio.count("Recebido"))
print("os que esta em Trânsito", rastreio.count("Em Trânsito"))

print("os códigos em trânsito são:", pacotes[2], pacotes[5])

indice=input("digite o indice ")
print(rastreio[2])

pacotes_ordenada=sorted(pacotes)
print(pacotes_ordenada)