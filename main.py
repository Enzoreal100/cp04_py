def cria_matriz(largura):
    matriz = []
    for i in range(largura):
        linha = []
        for j in range(largura):
            linha.append(0)
        matriz.append(linha)
    return matriz


def printa_matriz(matriz):
    for i in range(len(matriz)):
        print(matriz[i])


def fibornacci(matriz):
    fibornacci = [1, 1]
    for i in range(len(matriz) * len(matriz) - 2):
        atual = fibornacci[i] + fibornacci[i + 1]
        fibornacci.append(atual)
    return fibornacci


def checa_primo(fibornacci, matriz):
    os_dois = []
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(len(matriz)):
        for j in range(len(matriz)*len(matriz)):
            if fibornacci[i] == primos[j]:
               os_dois.append(fibornacci[i])
    return os_dois


def troca_fibornacci(matriz, fibornacci):
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = fibornacci[contador]
            contador += 1
    return matriz


def troca_item(matriz):

    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            contador = 0
            while contador <= len(primos):
                if matriz[i][j] == primos[contador]:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = 1
                contador +=1

    return matriz


matriz = cria_matriz(4)
printa_matriz(matriz)
print()
print(fibornacci(matriz))
print()
print(checa_primo(fibornacci(matriz), matriz))
print()
printa_matriz(troca_fibornacci(matriz, fibornacci(matriz)))
printa_matriz(troca_item(matriz))