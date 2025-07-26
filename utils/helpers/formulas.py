from array import ArrayType
import numpy as np
from utils.helpers.arrays import appendArray
from utils.validations.selector import validateSelector
from utils.validations.files import validateFormula
from utils.repositories.FileManager import FileManager
from utils.repositories.Formula import Formula
from utils.repositories.Number import Number
import math


def checkIsMatrix(fileManager: FileManager) -> bool:
    print("Tipos de datos:")
    print("- 1. Matrices")
    print("- 2. Numeros")
    choice = validateSelector(1, 2, "Elija el tipo de dato a usar (1-2): ", fileManager)
    return True if choice == 1 else False


def getFormulas(fileContent: ArrayType[ArrayType[str]], manager: FileManager, isMatrix: bool, elems: ArrayType[ArrayType[Number | int]]) -> ArrayType[ArrayType[Formula]]:
    formulas = np.array([])
    for i in range(len(fileContent)):
        fileFormulas = np.array([])
        for j in range(len(fileContent[i])):
            if isMatrix:
                formula = validateFormula(fileContent[i][j], manager, isMatrix)
                fileFormulas = appendArray(fileFormulas, formula)
            else:
                for _ in range(math.ceil(len(elems) / 3)):
                    formula = validateFormula(fileContent[i][j], manager, isMatrix)
                    fileFormulas = appendArray(fileFormulas, formula)
        formulas = appendArray(formulas, fileFormulas)
    return formulas
