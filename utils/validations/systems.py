from utils.repositories.NumericSystem import NumericSystem
from utils.repositories.FileManager import FileManager
from array import ArrayType


def validatePossibleSystems(systemManager: NumericSystem, value: str, fileManager: FileManager) -> ArrayType[str]:
    try:
        systemManager.setNumber(value)
        return systemManager.getPossibleSystems()
    except Exception as error:
        from utils.proccess.errors import createLogFile
        createLogFile(fileManager, error, error.__traceback__, value)
        return None
