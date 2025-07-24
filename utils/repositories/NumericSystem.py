import numpy as np
from array import ArrayType


class NumericSystem:
    """Representación de un sistema numérico.

    Attributes:
        number (str): Número en texto plano.
    """
    __number = "0"

    def __init__(self):
        self.__number = "0"

    def setNumber(self, number: str) -> None:
        """Establece el número.

        Args:
            number (str): Número en texto plano.
        """
        if len(number) == 0:
            raise Exception("Manage-Error: Debe ingresar un numero")
        self.__number = self.__utilNumber(number)

    def __isDecimal(self, number: str) -> str:
        """Valida si el número es decimal.

        Args:
            number (str): Número en texto plano.

        Returns:
            str: Si el número es decimal.
        """
        decimal_chars = "0123456789"
        for char in number:
            if char not in decimal_chars:
                return ""
        return "Decimal"

    def __isHex(self, number: str) -> str:
        """Valida si el número es hexadecimal.

        Args:
            number (str): Número en texto plano.

        Returns:
            str: Si el número es hexadecimal.
        """
        hex_chars = "0123456789ABCDEF"
        for char in number:
            if char.upper() not in hex_chars:
                return ""
        return "Hexadecimal"

    def __isBinary(self, number: str) -> str:
        """Valida si el número es binario.

        Args:
            number (str): Número en texto plano.

        Returns:
            str: Si el número es binario.
        """
        binary_chars = "01"
        for char in number:
            if char not in binary_chars:
                return ""
        return "Binario"

    def getPossibleSystems(self) -> ArrayType[str]:
        """Devuelve los sistemas numericos posibles del número.

        Returns:
            ArrayType[str]: Sistemas posibles del número.
        """
        if "." in self.__number or "," in self.__number:
            separator = "." if "." in self.__number else ","
            possibleBases = np.array([None, None])
            sides = np.array(self.__number.split(separator))
            for i in range(len(sides)):
                isDecimal = self.__isDecimal(sides[i])
                isHex = self.__isHex(sides[i])
                isBinary = self.__isBinary(sides[i])
                bases = np.array([isDecimal, isHex, isBinary])
                possibleBases[i] = bases[bases != ""]
            return np.intersect1d(possibleBases[0], possibleBases[1])
        else:
            isDecimal = self.__isDecimal(self.__number)
            isHex = self.__isHex(self.__number)
            isBinary = self.__isBinary(self.__number)
            bases = np.array([isDecimal, isHex, isBinary])
            return bases[bases != ""]

    def __utilNumber(self, number: str) -> str:
        """Valida el número ingresado.

        Args:
            number (str): Número en texto plano.

        Returns:
            str: Número en texto plano.

        Raises:
            Exception: Si el número ingresado no es valido.
        """
        chars_allowed = "0123456789ABCDEF.,"
        for char in number:
            if char.upper() not in chars_allowed:
                raise Exception(
                    f"Manage-Error: El numero {number} ingresado no es valido")
        if number.startswith((".", ",")) or number.endswith((".", ",")):
            raise Exception(
                f"Manage-Error: El numero {number} ingresado no es valido")
        separatorCount = number.count(".") + number.count(",")
        if separatorCount > 1:
            raise Exception(
                f"Manage-Error: El numero {number} ingresado no es valido")
        if number == "0":
            return "0"
        else:
            return number.lstrip("0")
