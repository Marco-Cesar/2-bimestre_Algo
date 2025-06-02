numero = (5, 8, 12, 8, 7, 8, 3)
#para ser uma tupla precisa estar entre paranteses!!!!!
print("tupal original:", numero)
#imprimindo para o usuario a tupla original, sem manipulações
print("tamanho da tupla:", len(numero))
print("acessando pelo indice:", numero[2])
#escolhendo qual item será mostradp atraves do indice, lembrando que começa do zero
print("fazerdo um slicing do 2 ao 5:", numero[2:5])
#o slicing ele não pega o ultimo item definido no recorto
print("Quantas vezes o numero 8 repete:", numero.count(8))
print("posição da primera ocorrencia do numero 7:", numero.index(7))
minimo_tupla=min(numero)
print("o menor numero da tupla", minimo_tupla)
maximo_tupla=max(numero)
print("o maio numero da tupla", maximo_tupla)
print("soma dos elemento da tupla", sum(numero))
tuple_ordenada=sorted(numero)
print("os numeros em ordem utilizado o metodo sorted", tuple_ordenada)
print("o numero 4 esta na tupla???", 4 in numero)
numero2=(15, 20)
tuple_concatenada=numero+numero2
print("a concatenação das tuplas 1 e 2 resulta na nova tupla:", tuple_concatenada)
tuple_duplicada=numero*2
print(tuple_duplicada)