from repositories.errors.AbsoluteError import AbsoluteError


class RelativeError(AbsoluteError):
    """Representación de un error relativo.

    Attributes:
        value (float): Valor original.
        aproxValue (float): Valor aproximado.
        error (float): Error relativo.
    """

    def __init__(self, value: float, aproxValue: float):
        super().__init__(value, aproxValue)

    def getError(self) -> float:
        """Devuelve el error relativo.

        Returns:
            float: Error relativo.
        """
        self._calcRelError()
        return self._error

    def _calcRelError(self) -> None:
        """Calcula el error relativo.

        Returns:
            float: Error relativo.
        """
        if self._value == 0:
            raise Exception(
                "Manage-Error: El valor no puede ser cero para calcular el error relativo")
        self._error = super().getAbsError() / abs(self._value)
