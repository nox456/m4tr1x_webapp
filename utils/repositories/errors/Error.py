class Error:
    """Representación de un error base.

    Attributes:
        value (float): Valor original.
        error (float): Error.
    """
    _error = 0.0
    _value = 0.0

    def __init__(self, value):
        if value is None:
            raise Exception("Manage-Error: Debe ingresar un valor")
        self._value = value

    def setValue(self, value):
        """Establece el valor.

        Args:
            value (float): Valor a evaluar.
        """
        if value is None:
            raise Exception("Manage-Error: Debe ingresar un valor")
        self._value = value

    def getValue(self):
        """Devuelve el valor.

        Returns:
            float: Valor a evaluar.
        """
        return self._value

    def getError(self):
        """Devuelve el error.

        Returns:
            float: Error.
        """
        self._calcError()
        return self._error

    def _calcError(self):
        """Calcula el error (metodo abstracto).

        Returns:
            float: Error.
        """
        pass