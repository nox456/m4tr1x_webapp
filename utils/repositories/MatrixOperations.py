import numpy as np
from array import ArrayType


class MatrixOperations:
    """Clase que realiza operaciones sobre matrices

    Attributes:
        __matrix (np.array): Matriz a operar
        __operations (str): Operaciones realizadas
    """

    __matrix = np.array([[]])
    __operations = ""

    def __init__(self, matrix: ArrayType[ArrayType[int]] = np.array([[]])):
        self.__matrix = matrix

    def setMatrix(self, matrix: ArrayType[ArrayType[int]]) -> None:
        """Establece la matriz a operar

        Args:
            matrix (ArrayType[ArrayType[int]]): Matriz a operar
        """
        self.__matrix = matrix

    def getMatrix(self) -> ArrayType[ArrayType[int]]:
        """Devuelve la matriz a operar

        Returns:
            ArrayType[ArrayType[int]]: Matriz a operar
        """
        return self.__matrix

    def getOperations(self) -> str:
        """Devuelve las operaciones realizadas

        Returns:
            str: Operaciones realizadas
        """
        return self.__operations

    def __swapRow(self) -> ArrayType[ArrayType[int]]:
        """Intercambia las filas de la matriz

        Returns:
            ArrayType[ArrayType[int]]: Matriz con las filas intercambiadas
        """
        if len(self.__matrix[0]) < 2:
            return self.__matrix
        newMatrix = np.array([[i for i in row] for row in self.__matrix])
        newMatrix[0] = self.__matrix[1]
        newMatrix[1] = self.__matrix[0]
        return newMatrix

    def __swapColumn(self) -> ArrayType[ArrayType[int]]:
        """Intercambia las columnas de la matriz

        Returns:
            ArrayType[ArrayType[int]]: Matriz con las columnas intercambiadas
        """
        if len(self.__matrix[1]) < 2:
            return self.__matrix
        newMatrix = np.array([[i for i in row] for row in self.__matrix])

        for i in range(len(newMatrix)):
            newMatrix[i, 0] = np.array(self.__matrix)[i, 1]
            newMatrix[i, 1] = np.array(self.__matrix)[i, 0]
        return newMatrix

    def __lambdaMult(self, a: int = 2) -> ArrayType[ArrayType[int]]:
        """Multiplica la matriz por un valor lambda

        Args:
            a (int, optional): Valor lambda. Defaults to 2.

        Returns:
            ArrayType[ArrayType[int]]: Matriz multiplicada por lambda
        """
        newMatrix = np.array([[i for i in row] for row in self.__matrix])

        for i in range(len(newMatrix[0])):
            newMatrix[0][i] = newMatrix[0][i]*a
        return newMatrix

    def __linearCombRow(self, a: int = 2) -> ArrayType[ArrayType[int]]:
        """Suma las filas de la matriz

        Args:
            a (int, optional): Valor a sumar. Defaults to 2.

        Returns:
            ArrayType[ArrayType[int]]: Matriz sumada
        """
        newMatrix = np.array([[i for i in row] for row in self.__matrix])

        for i in range(len(newMatrix[0])):
            newMatrix[0][i] += newMatrix[1][i]*a
        return newMatrix

    def doOperations(self, matrix: ArrayType[ArrayType[int]]) -> str:
        """Realiza las operaciones sobre la matriz

        Args:
            matrix (ArrayType[ArrayType[int]]): Matriz a operar

        Returns:
            str: Operaciones realizadas
        """
        if len(matrix) <= 1:
            raise ValueError("Matriz invalida")
        if len(matrix[0]) <= 1:
            raise ValueError("Matriz invalida")
        self.__matrix = matrix.copy()
        self.__operations = ""
        m = self.__swapRow()
        m = self.__swapColumn()
        self.__operations += "cambio"
        m = self.__lambdaMult()
        self.__operations += "; multLambda"
        m = self.__linearCombRow()
        self.__operations += "; combinacion"
        if len(self.__operations) == 0:
            self.__operations = "No hay operaciones disponibles"

        return self.__operations
