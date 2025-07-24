import numpy as np
from helpers.arrays import appendArray
from typing import TextIO
from array import ArrayType


class FileEntry:
    """La representación de un archivo unico.

    Attributes:
        name (str): Nombre del archivo.
        path (str): Ruta del archivo.
        content (ArrayType[str]): Contenido del archivo.
    """
    __name = ""
    __path = ""
    __content = np.array([])

    def __init__(self, name: str, rawContent: TextIO, path: str = "."):
        self.__name = name
        self.__path = path
        self.__content = self.__parseContent(rawContent)

    def __parseContent(self, rawContent: TextIO) -> ArrayType[str]:
        """Convierte el contenido de un archivo a un array de strings.

        Args:
            rawContent (TextIO): Contenido del archivo.

        Returns:
            ArrayType[str]: Array de strings con las lineas del archivo.
        """
        content = np.array([])
        for line in rawContent:
            content = appendArray(content, line.decode("utf-8").strip())
        if len(content) == 0:
            raise Exception("FileContent-Error: El archivo está vacío")
        return content

    def getContent(self) -> ArrayType[str]:
        """Devuelve el contenido del archivo.

        Returns:
            ArrayType[str]: Array de strings con las lineas del archivo.
        """
        return self.__content

    def getName(self) -> str:
        """Devuelve el nombre del archivo.

        Returns:
            str: Nombre del archivo.
        """
        return self.__name
    
    def setContent(self, content):
        self.__content = content

    def setName(self, name):
        self.__name = name
