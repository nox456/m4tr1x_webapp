from utils.validations.valFigs import validateFigures
from utils.repositories.SigFigures import SigFigures
from utils.repositories.FileManager import FileManager
from utils.repositories.Number import Number
from array import ArrayType


def getSigFigs(figuresManager: SigFigures, numbers: ArrayType[ArrayType[Number]], fileManager: FileManager) -> None:
    for number in numbers:
        if number.isValid():
            sigFigures = validateFigures(figuresManager, number.getValue(), fileManager)
            if sigFigures is not None:
                number.setFigs(sigFigures)
