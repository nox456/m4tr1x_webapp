from utils.proccess.files import selectFiles, createResultFile, selectFormulas, createFormulasResultFile, getFilesContent
from utils.proccess.numbers import getNumbers, setSystems, generateResultsFromFormulas, setOperations
from utils.proccess.matrixConverter import convert
from utils.proccess.figures import getSigFigs
from utils.repositories.NumericSystem import NumericSystem
from utils.repositories.SigFigures import SigFigures
from utils.repositories.FileManager import FileManager
from utils.helpers.formulas import checkIsMatrix, getFormulas
from utils.repositories.ElementalOperations import ElementalOperations
from utils.repositories.MatrixOperations import MatrixOperations
from utils.validations.gaussValidations import validateJordan, validateSeidel, instanceValidationJordan, instanceValidationSeidel


def preProcess() -> None:
    path = "./utils/storage/sources/"
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
        "./utils/storage/results/")
    createResultFile(fileManager, numbers, matrices,
                    matrixManager, resultJordan, resultSeidel)

    #isMatrix = checkIsMatrix(fileManager)
    isMatrix = True

    formulasEntries = selectFormulas(fileManager, isMatrix)

    if formulasEntries is None:
        print("-- PROGRAMA TERMINADO --")
        return

    formulaContent = getFilesContent(formulasEntries)

    formulas = getFormulas(formulaContent, fileManager, isMatrix,
                        matrices if isMatrix else numbers)

    generateResultsFromFormulas(formulas, numbers, matrices, fileManager, isMatrix)

    fileManager.setRouter("./utils/storage/results/")
    createFormulasResultFile(fileManager, formulas, formulasEntries)

    print("-- PROGRAMA TERMINADO --")

