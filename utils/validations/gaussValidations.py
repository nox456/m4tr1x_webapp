from repositories.GaussMatrixOp import GaussMatrixOp
from repositories.SeidelMatrixOp import SeidelMatrixOp


def validateJordan(matrix, manager):
    try:
        return matrix.startOperation()
    except Exception as error:
        from proccess.errors import createLogFile
        print(error)
        createLogFile(manager, error, error.__traceback__, matrix.getMatrix())


def validateSeidel(matrix, manager):
    try:
        return matrix.startOperation()
    except Exception as error:
        from proccess.errors import createLogFile
        print(error)
        createLogFile(manager, error, error.__traceback__, matrix.getMatrix())


def instanceValidationJordan(matrices, manager):
    try:
        matricesGauss = GaussMatrixOp(matrices)
        return matricesGauss
    except Exception as error:
        from proccess.errors import createLogFile
        print(error)
        createLogFile(manager, error, error.__traceback__, matrices)


def instanceValidationSeidel(matrices, manager):
    try:
        matricesGauss = SeidelMatrixOp(matrices)
        return matricesGauss
    except Exception as error:
        from proccess.errors import createLogFile
        print(error)
        createLogFile(manager, error, error.__traceback__, matrices)
