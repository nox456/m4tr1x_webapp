import numpy as np
from array import ArrayType


class Number:
    """Representación de un número.

    Attributes:
        value (str): Valor del número.
        isValid (bool): Indica si el número es válido.
        systems (ArrayType[str]): Sistemas numericos del número.
        sigFigs (str): Cifras significativas del número.
        ops (str): Operaciones del número.
    """
    __value = ""
    __isValid = False
    __systems = np.array([])
    __sigFigs = 0
    __ops = ""

    def __init__(self, value: str, validate: bool = True):
        # Convertir ',' a '.' antes de procesar
        value = value.replace(',', '.')
        self.__value = self.__utilValue(value) if validate else value
        self.__systems = np.array([])
        self.__sigFigs = 0
        self.__ops = ""

    def isValid(self) -> bool:
        """Devuelve si el número es válido.

        Returns:
            bool: Indica si el número es válido.
        """
        return self.__isValid

    def getValue(self) -> str:
        """Devuelve el valor del número.

        Returns:
            str: Valor del número.
        """
        return self.__value

    def setSystems(self, systems: ArrayType[str]) -> None:
        """Establece los sistemas numericos del número.

        Args:
            systems (ArrayType[str]): Sistemas numericos del número.
        """
        self.__systems = systems

    def getSystems(self) -> ArrayType[str]:
        """Devuelve los sistemas numericos del número.

        Returns:
            ArrayType[str]: Sistemas numericos del número.
        """
        return self.__systems

    def setFigs(self, figs: str) -> None:
        """Establece las cifras significativas del número.

        Args:
            figs (str): Cifras significativas del número.
        """
        self.__sigFigs = figs

    def getFigs(self) -> str:
        """Devuelve las cifras significativas del número.

        Returns:
            str: Cifras significativas del número.
        """
        return self.__sigFigs

    def setOperations(self, operations: str) -> None:
        """Establece las operaciones del número.

        Args:
            operations (str): Operaciones del número.
        """
        self.__ops = operations

    def getOperations(self) -> str:
        """Devuelve las operaciones del número.
        Returns:
            str: Operaciones del número.
        """
        return self.__ops

    def __utilValue(self, value: str) -> str:
        """Valida el valor ingresado.

        Args:
            value (str): Valor del número.

        Returns:
            str: Valor del número.

        Raises:
            Exception: Si el valor ingresado no es válido.
        """
        chars_allowed = "-0123456789ABCDEF."
        for char in value:
            if char.upper() not in chars_allowed:
                raise Exception(
                    f"Manage-Error: El numero {value} ingresado no es valido")
        if value.startswith(".") or value.endswith("."):
            raise Exception(
                f"Manage-Error: El numero {value} ingresado no es valido")
        if value.count(".") > 1:
            raise Exception(
                f"Manage-Error: El numero {value} ingresado no es valido")
        self.__isValid = True
        return value

    def toDecimal(self):
        """Convierte el número a base decimal.

        Returns:
            int | float | None: Número en decimal.
        """
        if self.__value is None:
            return None
        value = 0
        hexDict = {
            "0": "0",
            "1": "1",
            "2": "2",
            "3": "3",
            "4": "4",
            "5": "5",
            "6": "6",
            "7": "7",
            "8": "8",
            "9": "9",
            "a": "10",
            "b": "11",
            "c": "12",
            "d": "13",
            "e": "14",
            "f": "15"
        }
        if "Decimal" in self.__systems:
            if "." in self.__value:
                value = float(self.__value)
            else:
                value = int(self.__value)
        elif "Hexadecimal" in self.__systems and "Binario" not in self.__systems:
            for i in range(len(str(self.__value))):
                exponent = len(str(self.__value)) - i - 1
                n = int(hexDict[str(self.__value)[i].lower()])
                value += n * 16 ** exponent
        elif "Binario" in self.__systems:
            for i in range(len(str(self.__value))):
                exponent = len(str(self.__value)) - i - 1
                n = int(str(self.__value)[i])
                value += n * 2 ** exponent
        return value
