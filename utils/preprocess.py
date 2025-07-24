from proccess.files import selectFiles, createResultFile, selectFormulas, createFormulasResultFile, getFilesContent
from proccess.numbers import getNumbers, setSystems, generateResultsFromFormulas, setOperations
from proccess.matrixConverter import convert
from proccess.figures import getSigFigs
from repositories.NumericSystem import NumericSystem
from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager
from helpers.formulas import checkIsMatrix, getFormulas
from repositories.ElementalOperations import ElementalOperations
from repositories.MatrixOperations import MatrixOperations
from validations.gaussValidations import validateJordan, validateSeidel, instanceValidationJordan, instanceValidationSeidel


def preProcess() -> None:
    path = "./src/storage/sources/"
    fileManager = FileManager(path)

    aux = matrices = convert(fileManager)

    if matrices is None or len(matrices) == 0:
        return

    matrixGauss = instanceValidationJordan(matrices, fileManager)
    resultJordan = validateJordan(matrixGauss, fileManager)

    matrices = aux

    matrixGauss = instanceValidationSeidel(matrices, fileManager)
    resultSeidel = validateSeidel(matrixGauss, fileManager)

    matrixManager = MatrixOperations()

    files = selectFiles(fileManager)
    if files is None or len(files) == 0:
        print("-- PROGRAMA TERMINADO --")
        return
    content = getFilesContent(files)
    if len(content) == 0:
        print("Archivo vacío")
        return
    numbers = getNumbers(content, fileManager)
    if len(numbers) == 0:
        print("-- PROGRAMA TERMINADO --")
        return

    systemManager = NumericSystem()
    setSystems(numbers, systemManager, fileManager)

    figuresManager = SigFigures("0")
    getSigFigs(figuresManager, numbers, fileManager)

    operationManager = ElementalOperations()
    setOperations(numbers, operationManager)

    fileManager.setRouter(
        "./src/storage/results/")
    createResultFile(fileManager, numbers, matrices,
                     matrixManager, resultJordan, resultSeidel)

    isMatrix = checkIsMatrix(fileManager)

    formulasEntries = selectFormulas(fileManager, isMatrix)

    if formulasEntries is None:
        print("-- PROGRAMA TERMINADO --")
        return

    formulaContent = getFilesContent(formulasEntries)

    formulas = getFormulas(formulaContent, fileManager, isMatrix,
                           matrices if isMatrix else numbers)

    generateResultsFromFormulas(formulas, numbers, matrices, fileManager, isMatrix)

    fileManager.setRouter("./src/storage/results/")
    createFormulasResultFile(fileManager, formulas, formulasEntries)

    print("-- PROGRAMA TERMINADO --")

