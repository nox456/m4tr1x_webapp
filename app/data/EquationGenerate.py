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
        self.saveFormulas()

    def __generateRandomOperator(self):
        return random.choice(['+', '-', '*', '/'])
    
    def __generateRandomMember(self):
        num = random.randint(1, 3)
        if num == 1:
            return "A"
        elif num == 2:
            return "B"
        else:
            return "C"
    
    def __generateFormula(self):
        elements = [self.__generateRandomMember() for _ in range(3)]
        operators = [self.__generateRandomOperator() for _ in range(random.randint(3, 5))]
        
        formulaParts = []
        for i in range(len(operators)):
            formulaParts.append(elements[i % len(elements)])
            formulaParts.append(operators[i])
        
        formulaParts.append(elements[-1])
        
        formula = ' '.join(formulaParts)
        
        if random.choice([True, False]):
            openPos = random.randint(0, len(formulaParts)//2)
            closePos = random.randint(openPos+1, len(formulaParts)-1)
            formula = (formula[:openPos*2] + '(' + formula[openPos*2:closePos*2] + ')' + formula[closePos*2:])
        
        return formula

    def saveFormulas(self):
        try:
            with open(os.path.join(self.__router, self.__nameArchive), 'w') as file:
                formula = self.__generateFormula()
                file.write(formula + '\n')
            print(f"Se generaro la fórmula en {self.__nameArchive}")
        except Exception as e:
            print(f"Error al generar fórmulas: {e}")

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