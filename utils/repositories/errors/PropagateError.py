from repositories.errors.Error import Error
import math


class PropagationError(Error):
    """Clase para el cálculo del error de propagación."""

    __propagationValue = 0.0

    def __init__(self, value, propagationValue):
        """Inicializa la clase PropagationError.

        Args:
            value (float): Valor real o de referencia.
            propagationValue (float): Valor a propagar.
        """
        super().__init__(value)
        self.__propagationValue = propagationValue

    def setPropagationValue(self, propagationValue):
        """Establece el valor de propagación.

        Args:
            propagationValue (float): Valor a propagar.

        Raises:
            Exception: Si no se ingresa un valor válido.
        """
        if propagationValue is None:
            raise Exception("Manage-Error: Debe ingresar un valor truncado")
        self.__propagationValue = propagationValue

    def getPropagationError(self):
        """Devuelve el error de propagación calculado.

        Returns:
            float: Error de propagación.
        """
        self._calcError()
        return self._error
    
    def __aproximate(self, x):
        """Calcula una aproximación para el valor de propagación.

        Args:
            x (float): Valor a aproximar.

        Returns:
            float: Valor aproximado.
        """
        return (x + 0.1) * 3 - 0.3

    def _calcError(self):
        """Calcula el error de propagación."""
        self.setPropagationValue(self.__aproximate(self.__propagationValue))
        self._error = abs(self._value - self.__propagationValue)