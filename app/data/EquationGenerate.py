import os
import random

class eqGenerator:

    __router = ""
    __nameArchive = ""

    def __init__(
        self, nameArchive="eqArchive.bin", router=os.getcwd()):
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

        self.__nameArchive = nameArchive
        self.__utilDirectory(router)

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

        self.__nameArchive

    def __setOrCreateFiles(self, nameArchive, content="", bool=False):

        if not nameArchive or len(nameArchive) == 0:
            raise Exception("Manage-Error: El nombre esta Vacio.")

        try:
            if not content or len(content) == 0:
                archive = open(self.__router + "\\" + nameArchive + ".txt", "x")
                return
            archive = open(os.path.join(self.__router,nameArchive), "a")

            if bool == True:
                archive.write(content + "\n")
            else:
                archive.write(content)

        except FileNotFoundError as e:
            print("Manage-Error: El archivo no ha sido encontrado", e)



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