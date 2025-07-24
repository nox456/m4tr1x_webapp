class SigFigures:
    """Representación de las cifras significativas de un número.

    Attributes:
        number (str): Número a analizar.
    """

    __isZero = True
    __number = ""

    def __init__(self, number: str):
        if (self.utilNumber(number)):
            self.__number = number
        else:
            raise Exception("Manage-Error: El numero está vacio.")

    def getNumber(self) -> str:
        """Devuelve el número a analizar.

        Returns:
            str: Número a analizar.
        """
        return self.__number

    def setNumber(self, number: str) -> None:
        """Establece el número a analizar.

        Args:
            number (str): Número a analizar.
        """
        if (self.utilNumber(number)):
            self.__number = number
        else:
            raise Exception("Manage-Error: El numero está vacio.")

    def operation(self) -> str:
        """Devuelve la operación a realizar.

        Returns:
            str: Operación a realizar.
        """
        num1, num2 = self.separateNumber()
        cont, fig = self.cantFigures(num1)
        cont2, fig2 = self.cantFigures(reversed(num2))
        cont += cont2
        rfig2 = fig2[::-1]
        fig += rfig2
        return self.mostrar(cont, fig)

    def separateNumber(self) -> tuple[str, str]:
        """Separa el número en dos partes.

        Returns:
            tuple[str, str]: Parte entera y decimal.
        """
        flag = False
        number1 = ""
        number2 = ""
        for digits in self.__number:
            if (digits != "." and digits != "." and not flag):
                number1 += digits
            else:
                flag = True
            if (flag):
                number2 += digits
        return number1, number2

    def cantFigures(self, num: str) -> tuple[int, str]:
        """Devuelve la cantidad de cifras y las cifras en si.

        Args:
            num (str): Número a analizar.

        Returns:
            tuple[int, str]: Cantidad de cifras y las cifras en si.
        """
        figures = ""
        cont = 0
        cantDots = 0
        for digit in num:
            if (digit != "0" and digit != "." and digit != ","):
                self.__isZero = False
            if (not self.__isZero):
                cont += 1
                figures += digit
            if (digit == "." or digit == ","):
                cantDots += 1
                cont -= 1
            if (cantDots >= 2):
                raise Exception("Manage-Error: Doble punto decimal")
        self.__isZero = True
        return cont, figures

    def mostrar(self, con: int, figures: str) -> str:
        """Devuelve la representación de las cifras en si.

        Args:
            con (int): Cantidad de cifras.
            figures (str): Cifras en si.

        Returns:
            str: Mensaje con las cifras significativas.
        """
        return "Cantidad de cifras: "+str(con)+" Cifras en si: "+figures

    def utilNumber(self, number: str) -> bool:
        """Valida si el número es válido.

        Args:
            number (str): Número a validar.

        Returns:
            bool: Indica si el número es válido.
        """
        if (number == ""):
            return False
        return True
