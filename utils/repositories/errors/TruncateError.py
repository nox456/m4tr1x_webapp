from repositories.errors.Error import Error
import math

class TruncateError(Error):
    """Representación de un error truncado.

    Attributes:
        value (float): Valor original.
        truncatedValue (float): Valor truncado.
        error (float): Error truncado.
    """
    __truncatedValue = 0.0
    __x = 0.0

    def __init__(self, value: float, truncatedValue: float):
        super().__init__(value)
        self.__truncatedValue = truncatedValue

    def setTruncatedValue(self, truncatedValue: float) -> None:
        """Establece el valor truncado.

        Args:
            truncatedValue (float): Valor truncado.
        """
        if truncatedValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor truncado")
        self.__truncatedValue = truncatedValue

    def getTruncateError(self) -> float:
        """Devuelve el error truncado.

        Returns:
            float: Error truncado.
        """
        self._calcError()
        return self._error
    
    def __aproximate(self, x, n):
        """Calcula la aproximación de la función coseno.

        Args:
            x (float): Valor de entrada.
            n (int): Número de términos a considerar.
        Returns:
            float: Aproximación del coseno.
        """

        sum = 0.0
        for i in range(n):
            sum += (-1)**i * (x**(2*i)) / math.factorial((2*i))
        return sum

    def _calcError(self) -> None:
        """Calcula el error truncado.

        Returns:
            float: Error truncado.
        """
        self.setTruncatedValue(self.__aproximate(self.__truncatedValue), 3)
        self._error = abs(self._value - self.__truncatedValue)

