from validations.valFigs import validateFigures
from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager
from repositories.Number import Number
from array import ArrayType


def getSigFigs(figuresManager: SigFigures, numbers: ArrayType[ArrayType[Number]], fileManager: FileManager) -> None:
    for number in numbers:
        if number.isValid():
            sigFigures = validateFigures(figuresManager, number.getValue(), fileManager)
            if sigFigures is not None:
                number.setFigs(sigFigures)
