from repositories.SigFigures import SigFigures
from repositories.FileManager import FileManager


def validateFigures(figuresManager: SigFigures, value: str, fileManager: FileManager) -> str:
    try:
        figuresManager.setNumber(value)
        return figuresManager.operation()
    except Exception as error:
        from proccess.errors import createLogFile
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
