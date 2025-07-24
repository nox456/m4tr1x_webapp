import numpy as np
from proccess.files import selectFiles, getFilesContent
from proccess.numbers import getNumbers, setSystems
from repositories.NumericSystem import NumericSystem
from array import ArrayType


def convert(manager):
    manager.setRouter("./src/storage/sources/")
    files = selectFiles(manager)
    if files is None:
        return
    filColums = np.array([None for _ in range(len(files))])
    matrices = np.array([None for _ in range(len(files))])
    for i in range(len(files)):
        filColums[i] = cantReg(files[i])
        matrices[i] = createMatrix(filColums[i])
    fillMatrix(files, matrices, filColums, manager)
    return matrices


def cantReg(file):
    filaColum = np.array([0, 0])
    if (file == ""):
        print("Objet-file: El archivo está vacio.")
        return filaColum
    file = file.getContent()
    camp = np.array([])
    cont = 0
    band = 0
    aux = 0
    for i in file:
        cont = cont + 1
        camp = i.split("#")
        if (band == 0):
            aux = len(camp)
            band = 1
        elif (len(camp) > aux):
            aux = len(camp)
    filaColum[0] = aux
    filaColum[1] = cont
    return filaColum


def createMatrix(filaColum: ArrayType[int]) -> ArrayType[ArrayType[int]]:
    matrix = np.array([np.array([0 for _ in range(filaColum[0])]) for _ in range(filaColum[1])])
    return matrix


def fillMatrix(files, matrix, filCol, manager):
    content = getFilesContent(files)
    if len(content) == 0:
        print("Archivo vacío")
        return
    numbers = getNumbers(content, manager, True)
    systemManager = NumericSystem()
    setSystems(numbers, systemManager, manager, True)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                if k < len(numbers[i][j]):
                    matrix[i][j][k] = numbers[i][j][k].toDecimal()
                else:
                    matrix[i][j][k] = 0
    return matrix
