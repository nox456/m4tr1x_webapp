import numpy as np
from utils.proccess.files import selectFormulas, getFilesContent
from utils.proccess.numbers import generateResultsFromFormulas
from utils.proccess.matrixConverter import convert
from utils.repositories.FileManager import FileManager
from utils.helpers.formulas import getFormulas
from utils.validations.gaussValidations import validateJordan, instanceValidationJordan


def proccessmatrix():
    path = "./utils/storage/sources/"
    fileManager = FileManager(path)

    matrices = convert(fileManager)

    if matrices is None or len(matrices) == 0:
        return
    
    isMatrix = True
    numbers = np.array([])
    
    formulasEntries = selectFormulas(fileManager, isMatrix)

    formulaContent = getFilesContent(formulasEntries)

    formulas = getFormulas(formulaContent, fileManager, isMatrix,matrices)

    result = generateResultsFromFormulas(formulas, numbers, matrices, fileManager, isMatrix)

    n=0

    for i in range(len(result)):
        if i%4 == 0:
            matrices[n]=matrixConverter(result[i])
            n+=1

    matrixGauss = instanceValidationJordan(matrices, fileManager)
    resultJordan = validateJordan(matrixGauss, fileManager)
    return resultJordan


def matrixConverter(s):
    valores = s.split('|')
    matriz = np.zeros((3, 3))
    n=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = float(valores[n])
            n+=1
    return matriz