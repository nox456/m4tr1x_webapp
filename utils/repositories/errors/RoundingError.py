from utils.repositories.errors.Error import Error


class RoundingError(Error):
    """Representación de un error de redondeo.

    Attributes:
        value (float): Valor original.
        roundedValue (float): Valor redondeado.
        error (float): Error de redondeo.
    """
    __roundedValue = 0.0

    def __init__(self, value: float, roundedValue: float):
        super().__init__(value)
        self.__roundedValue = roundedValue

    def getRoundingError(self) -> float:
        """Devuelve el error de redondeo.

        Returns:
            float: Error de redondeo.
        """
        self._calcError()
        return self._error

    def _calcError(self) -> None:
        """Calcula el error de redondeo.

        Returns:
            float: Error de redondeo.
        """
        self._error = abs(self._value - self.__roundedValue)
