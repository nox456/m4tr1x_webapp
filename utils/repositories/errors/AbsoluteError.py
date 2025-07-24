from repositories.errors.Error import Error


class AbsoluteError(Error):
    """Representación de un error absoluto.

    Attributes:
        value (float): Valor original.
        aproxValue (float): Valor aproximado.
        error (float): Error absoluto.
    """

    _aproxValue = 0.0

    def __init__(self, value: int, aproxValue: int):
        super().__init__(value)
        self._aproxValue = aproxValue

    def setAproxValue(self, aproxValue: int) -> None:
        """Establece el valor aproximado.

        Args:
            aproxValue (float): Valor aproximado.
        """
        if aproxValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor aproximado")
        self._aproxValue = aproxValue

    def getAproxValue(self) -> int:
        """Devuelve el valor aproximado.

        Returns:
            float: Valor aproximado.
        """
        return self._aproxValue

    def getAbsError(self) -> float:
        """Devuelve el error absoluto.

        Returns:
            float: Error absoluto.
        """
        self._calcAbsError()
        return self._error

    def _calcAbsError(self) -> float:
        """Calcula el error absoluto.

        Returns:
            float: Error absoluto.
        """
        self._error = abs(self._value - self._aproxValue)
