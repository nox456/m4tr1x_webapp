import numpy as np


def sumaMatrices(matrizA, matrizB):
    filas = len(matrizA)
    columnas = len(matrizA[0])
    matrizC = [[0 for _ in range(columnas)] for _ in range(filas)]
    if type(matrizA) is float or type(matrizA) is int:
        matrizA = [[matrizA for _ in range(columnas)] for _ in range(filas)]
    if type(matrizB) is float or type(matrizB) is int or matrizB is np.float64:
        matrizB = [[matrizB for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrizC[i][j] = matrizA[i][j] + matrizB[i][j]
    return matrizC


def multiMatrices(matrizA, matrizB):
    filasA = len(matrizA)
    columnasA = len(matrizA[0])
    columnasB = len(matrizB[0])
    matrizD = [[0 for _ in range(columnasB)] for _ in range(filasA)]
    if type(matrizA) is float or type(matrizA) is int:
        matrizA = [[matrizA for _ in range(columnasA)] for _ in range(filasA)]
    if type(matrizB) is float or type(matrizB) is int or matrizB is np.float64:
        matrizB = [[matrizB for _ in range(columnasB)] for _ in range(filasA)]
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                matrizD[i][j] += matrizA[i][k] * matrizB[k][j]
    return matrizD


def restaMatrices(matrizA, matrizB):
    filas = len(matrizA)
    columnas = len(matrizA[0])
    matrizC = [[0 for _ in range(columnas)] for _ in range(filas)]
    if type(matrizA) is float or type(matrizA) is int:
        matrizA = [[matrizA for _ in range(columnas)] for _ in range(filas)]
    if type(matrizB) is float or type(matrizB) is int or matrizB is np.float64:
        matrizB = [[matrizB for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrizC[i][j] = matrizA[i][j] - matrizB[i][j]
    return matrizC


def divideMatrices(matrizA, matrizB):
    filas = len(matrizA)
    columnas = len(matrizA[0])
    matrizC = [[0 for _ in range(columnas)] for _ in range(filas)]
    if type(matrizA) is float or type(matrizA) is int:
        matrizA = [[matrizA for _ in range(columnas)] for _ in range(filas)]
    if type(matrizB) is float or type(matrizB) is int or matrizB is np.float64:
        matrizB = [[matrizB for _ in range(columnas)] for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            matrizC[i][j] = matrizA[i][j] / matrizB[i][j]
    return matrizC
