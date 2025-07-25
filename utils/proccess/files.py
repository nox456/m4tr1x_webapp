from utils.validations.files import validateSourceFileName, validateFileEntry
import numpy as np
import random
from utils.repositories.FileManager import FileManager
from utils.repositories.FileEntry import FileEntry
from array import ArrayType
from utils.repositories.Number import Number
from utils.repositories.Formula import Formula
from utils.helpers.arrays import appendArray
from datetime import datetime
from utils.repositories.MatrixOperations import MatrixOperations
from utils.validations.operations import validateMatrixOperation


def selectFiles(manager: FileManager) -> ArrayType[FileEntry]:
    files = manager.listFiles()
    if len(files) == 0:
        print("No hay archivos disponibles")
        return None
    else:
        filesEntries = np.array([])
        for file in files:
            if validateSourceFileName(file, manager) is None:
                continue
            rawContent = manager.openFile(file)
            if rawContent is None:
                continue
            fileEntry = validateFileEntry(file, rawContent, manager)
            if fileEntry is None:
                continue
            filesEntries = appendArray(filesEntries, fileEntry)
        return filesEntries


def createResultNumbersFiles(manager: FileManager, fileName: str, numbers: ArrayType[ArrayType[Number]]) -> None:
    for number in numbers:
        if number.isValid():
            systems = number.getSystems()
            joinedSystems = ""
            for system in systems:
                joinedSystems = f"{joinedSystems},{system}"

            resultLine = f"{number.getValue()}#{joinedSystems[1:]}#{
                number.getFigs()}#{number.getOperations()}\n"
        else:
            resultLine = f"{
                number.getValue()} -> No pertenece a ningun sistema numerico\n"
        manager.writeFile(fileName, resultLine)


def getFilesContent(files: ArrayType[FileEntry]) -> ArrayType[ArrayType[str]]:
    content = np.array([])
    for file in files:
        content = appendArray(content, file.getContent())
    return content


def createResultMatrixFile(manager: FileManager, fileName: str,  matrices, matrixManager, jordan, seidel):
    for i in range(len(matrices)):
        if len(matrices[i]) == 0:
            resultLine = "Matriz vacia\n"
        else:
            resultLine = ""
            for row in matrices[i]:
                rowValues = [str(num) for num in row]
                resultLine += " | ".join(rowValues) + "\n"
        manager.writeFile(fileName, resultLine)
        manager.writeFile(fileName, "Operaciones: ")
        operations = validateMatrixOperation(matrices[i], matrixManager)
        manager.writeFile(fileName, str(operations) + "\n")
        resultLine = "Resultado por Gauss-Jordan: " + \
            str(jordan[i]) + ".   Resultado por Gauss-Seidel: " + str(seidel[i]) + "\n"
        manager.writeFile(fileName, resultLine)


def selectFormulas(manager: FileManager, isMatrix: bool) -> ArrayType[FileEntry]:
    manager.setRouter("./utils/storage/formulas/")
    formulasFiles = manager.listFiles()
    if len(formulasFiles) == 0:
        print("No hay formularios disponibles")
        return None
    else:
        formulas = np.array([])
        for file in formulasFiles:
            if validateSourceFileName(file, manager) is None:
                continue
            rawContent = manager.openFile(file)
            if rawContent is None:
                continue
            formula = validateFileEntry(file, rawContent, manager)
            if formula is None:
                continue
            formulas = appendArray(formulas, formula)
        return formulas


def createFormulasResultFile(manager: FileManager, formulas: ArrayType[Formula], formulaFiles: ArrayType[FileEntry]) -> None:
    for i in range(len(formulaFiles)):
        sourceFileAttributes = np.array(
            formulaFiles[i].getName().rstrip(".bin").split("_"))
        newSerial = random.randint(1000, 9999)
        resultFileName = f"{sourceFileAttributes[2]}_{
            sourceFileAttributes[1]}_{newSerial}.txt"
        for formula in formulas[i]:
            if not formula.isValid():
                resultLine = f"Formula invalida -> {formula.getRaw()}\n"
                manager.writeFile(resultFileName, resultLine)
            else:
                if formula.isMatrix():
                    resultLine = f"{formula.getRaw()}\n{formula.getResult()}\n"
                else:
                    resultLine = f"{formula.getRaw()}#{formula.getValues()}#{
                        formula.getResult()}\n"
                manager.writeFile(resultFileName, resultLine)


def createResultFile(manager: FileManager, numbers: ArrayType[ArrayType[Number]], matrices: ArrayType[ArrayType[ArrayType[int]]], matrixManager: MatrixOperations, jordan, seidel) -> None:
    now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    serial = random.randint(1000, 9999)
    resultFileName = f"result_{now}_{serial}.txt"
    createResultNumbersFiles(manager, resultFileName, numbers)
    manager.writeFile(resultFileName, "\n-----------------------------------------\n\n")
    createResultMatrixFile(manager, resultFileName, matrices,
                           matrixManager, jordan, seidel)
