from utils.repositories.FileManager import FileManager
from utils.proccess.errors import createLogFile


def validateSelector(min: int, max: int, text: str, fileManager: FileManager) -> int:
    while True:
        try:
            value = int(input(text + "(-1) para salir: "))
            if value == -1:
                return -1
            if value < min or value > max:
                raise Exception("El valor debe estar entre los límites")
            return value
        except Exception as error:
            print(error)
            createLogFile(fileManager, error, error.__traceback__, value)

def validateNumber(text) -> int:
    while True:
        try:
            value = int(input(text))
            if value == -1:
                return -1
            if value < min or value > max:
                raise Exception("El valor debe estar entre los límites")
            return value
        except Exception as error:
            print(error)
