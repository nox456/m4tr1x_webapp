from utils.helpers.arrays import appendArray
from utils.validations.files import validateFileLine, validateFileElement
from utils.validations.systems import validatePossibleSystems
import numpy as np
from utils.repositories.FileManager import FileManager
from utils.repositories.NumericSystem import NumericSystem
from utils.repositories.Number import Number
from utils.repositories.Formula import Formula
from utils.repositories.ElementalOperations import ElementalOperations
from array import ArrayType
import math
from utils.validations.operations import validateOperations


def getNumbers(fileContent: ArrayType[ArrayType[str]], manager: FileManager, inMatrix: bool = False) -> ArrayType[ArrayType[Number]]:
    numbers = np.array([])
    for i in range(len(fileContent)):
        fileNumbers = np.array([])
        for j in range(len(fileContent[i])):
            line = validateFileLine(fileContent[i][j], manager)
            if line is not None:
                lineNumbers = line.split("#")
                numbersLines = np.array([])
                for k in range(len(lineNumbers)):
                    number = validateFileElement(lineNumbers[k], manager)
                    if inMatrix:
                        numbersLines = appendArray(numbersLines, number)
                    else:
                        numbers = appendArray(numbers, number)
                if inMatrix:
                    fileNumbers = appendArray(fileNumbers, numbersLines)
        if inMatrix:
            numbers = appendArray(numbers, fileNumbers)
    return numbers


def generateResultsFromFormulas(formulas: ArrayType[ArrayType[Formula]], numbers: ArrayType[ArrayType[Number]], matrices: ArrayType[ArrayType[ArrayType[int]]], manager: FileManager, isMatrix: bool) -> None:
    if isMatrix:
        for i in range(len(formulas)):
            for j in range(len(formulas[i])):
                for matrix in matrices:
                    formulas[i][j].evaluateMatrixFormula(matrices, manager)
    else:
        for i in range(len(formulas)):
            j = 0
            while j < len(formulas[i]):
                numbersParts = getNumbersTrios(numbers)
                for i2 in range(len(numbersParts)):
                    formulas[i][j].evaluateNumbersFormula(numbersParts[i2])
                    j += 1



def getNumbersTrios(numbers: ArrayType[Number]) -> ArrayType[ArrayType[Number]]:
    allNumbers = np.array(numbers)
    parts = np.array_split(allNumbers, math.ceil(len(numbers) / 3))
    return parts


def setOperations(numbers: ArrayType[Number], operationsManager: ElementalOperations) -> None:
    for number in numbers:
        if number.isValid():
            operations = validateOperations(
                operationsManager, number.getValue(), number.getSystems())
            if operations is not None:
                number.setOperations(operations)


def setSystems(numbers: ArrayType[ArrayType[Number]], systemManager: NumericSystem, manager: FileManager, inMatrix: bool = False) -> None:
    if inMatrix:
        for fileNumbers in numbers:
            for number in fileNumbers:
                for i in range(len(number)):
                    if number[i].isValid():
                        systems = validatePossibleSystems(
                            systemManager, number[i].getValue(), manager)
                        if systems is not None:
                            number[i].setSystems(systems)
    else:
        for number in numbers:
            if number.isValid():
                systems = validatePossibleSystems(
                    systemManager, number.getValue(), manager)
                if systems is not None:
                    number.setSystems(systems)
