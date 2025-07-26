import os
import random
from datetime import datetime

class archiveGenerator:
    __router = ""
    __nameArchive = ""

    def __init__(self, nameArchive="generalArchive", router=os.getcwd()):
        """
        Crear o modificar archivos.

        ->@param: string [archive.extension]
        ->@param: string router = C:\\folder1\\folder2\\folder or "C:\folder\folder\folder" or C:/folder/folder/folder
        ->@return: Void
        """
        if not router or len(router) == 0:
            raise Exception("Manage-Error: La ruta es vacia.")

        if len(nameArchive) == 0 or not nameArchive:
            raise Exception("Manage-Error: La ruta es vacia.")

        self.__utilDirectory(router)
        fecha = datetime.now().strftime("%d-%m-%Y")
        for i in range(3):
            self.__nameArchive = nameArchive+"_"+fecha+"_serial"+str(i)+".bin"
            self.archiveDataGenerator()

    def setRouter(self, router):
        """
        Cambio de ruta existente

        ->@param: string router = C:\\folder1\\folder2\\folder or "C:\folder\folder\folder" or C:/folder/folder/folder
        ->@return: Void
        """
        if not router or len(router) == 0:
            raise Exception("Manage-Error: La ruta es vacia.")
        self.__utilDirectory(router)

    def setName(self, nameArchive):
        """
        Cambio de ruta existente

        ->@param: string [archive.extension]
        ->@return: Void
        """
        if not nameArchive or len(nameArchive) == 0:
            raise Exception("Manage-Error: La ruta es vacia.")

        self.__nameArchive = nameArchive

    def __setOrCreateFiles(self, nameArchive, content="", bool=False):

        if not nameArchive or len(nameArchive) == 0:
            raise Exception("Manage-Error: El nombre esta Vacio.")

        try: 
            if self.cantReg() >= 3 and self.cantElements() >3:
                os.remove(self.__router + nameArchive)
                archive = open(self.__router + nameArchive, "w")
                if bool == True:
                    archive.write(content + "\n")
                else:
                    archive.write(content)
            archive = open(os.path.join(self.__router,nameArchive), "a") 

            if bool == True:
                archive.write(content + "\n")
            else:
                archive.write(content)

        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)

    def archiveDataGenerator(self, row=3, colum=3):
        """
        Genera archivo con datos aleatorios.

        ->@param: Float/Float [data default = 3]
        ->@return: Void
        """
        arrayBi = []

        if row > 0 and colum > 0:
            arrayBi = [
                [random.randint(-30, 30) for _ in range(colum)] for _ in range(row)
            ]

            for i in range(len(arrayBi)):
                for j in range(len(arrayBi[0])):
                    if j == (len(arrayBi[0]) - 1):
                        self.__setOrCreateFiles(self.__nameArchive, str(arrayBi[i][j]), i < (len(arrayBi) - 1),)
                    else:
                        self.__setOrCreateFiles(self.__nameArchive, str(arrayBi[i][j]) + "#")

    def __utilDirectory(self, router):

        if not os.path.exists(router):
            raise FileNotFoundError(
                f"Manage-Error: El directorio '{router}' no existe."
            )
        elif os.path.exists(router) and not os.path.isdir(router):
            raise NotADirectoryError(
                f"Manage-Error: La ruta '{router}' no es un directorio."
            )
        self.__router = router

    def cantReg(self):
        if not self.__nameArchive or len(self.__nameArchive) == 0:
            raise Exception("Manage-Error: El nombre esta Vacio.")

        try:
            with open(os.path.join(self.__router, self.__nameArchive), 'r') as file:
                return len(file.readlines())
        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)
            return 0

    def cantElements(self):
        if not self.__nameArchive or len(self.__nameArchive) == 0:
            raise Exception("Manage-Error: El nombre esta Vacio.")

        try:
            with open(os.path.join(self.__router, self.__nameArchive), 'r') as file:
                lines = file.readlines()
                if not lines:
                    return 0
                ultimo_registro = lines[-1].strip()
                if not ultimo_registro:
                    return 0
                return len(ultimo_registro.split('#'))
        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)
            return 0