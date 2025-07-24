import numpy as np
from helpers.arrays import appendArray
from validations.operations import validateGaussOperation


class GaussMatrixOp:
    """Clase para operaciones con matrices usando el método de Gauss."""

    __matrices = np.array([])

    def __init__(self, mat):
        """Inicializa la clase GaussMatrixOp.

        Args:
            mat (array): Arreglo de matrices a operar.

        Raises:
            ValueError: Si no se reciben matrices.
        """
        if len(mat) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = mat

    # setters
    def setMatrix(self, matrix):
        """Establece las matrices a operar.

        Args:
            matrix (array): Arreglo de matrices.

        Raises:
            ValueError: Si no se reciben matrices o es None.
        """
        if matrix == None:
            raise ValueError("Error: Es necesario tener las matrices")
        if len(matrix) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = matrix

    # getters
    def getMatrix(self):
        """Devuelve las matrices almacenadas.

        Returns:
            array: Matrices almacenadas.
        """
        return self.__matrices

    # methods
    def operation(self, matrix):
        """Resuelve un sistema de ecuaciones lineales por el método de Gauss.

        Args:
            matrix (array): Matriz aumentada del sistema.

        Returns:
            array: Solución del sistema.

        Raises:
            ValueError: Si la matriz tiene infinitas soluciones.
        """
        A = np.array(matrix, dtype=float)
        n = len(A)
        for i in range(n):
            if A[i, i] == 0:
                raise ValueError("Esta matriz tiene infinitas soluciones")
            A[i] = A[i] / A[i, i]
            for j in range(n):
                if i != j:
                    A[j] = A[j] - A[j, i] * A[i]
        return A[:, -1]

    def addToMatrix(self, matrix):
        """Agrega una columna adicional a la matriz (rellena con 1 al final de cada fila).

        Args:
            matrix (array): Matriz original.

        Returns:
            array: Matriz con columna adicional.
        """
        matrixAux = np.zeros((len(matrix), len(matrix[0]) + 1))
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrixAux[i][j] = matrix[i][j]
            matrixAux[i][-1] = 1
        return matrixAux

    def cantMatrx(self):
        """Devuelve la cantidad de matrices almacenadas.

        Returns:
            int: Cantidad de matrices.
        """
        n = 0
        for rows in self.__matrices:
            n += 1
        return n

    def checkMatrix(self, matrix):
        """Verifica si la matriz es un arreglo de Numpy y si es cuadrada.

        Args:
            matrix (np.ndarray): Matriz a verificar.

        Returns:
            str: Mensaje de advertencia si no es cuadrada, vacío si es válida.

        Raises:
            ValueError: Si la matriz no es un arreglo de NumPy.
        """
        if not isinstance(matrix, (np.ndarray)):
            raise ValueError("La matriz debe ser un arreglo de NumPy.")
        if len(matrix) != len(matrix[0]):
            return "Al no ser una matriz cuadrada, tendra o infinitas soluciones o ninguna solucion"
        return ""

    def startOperation(self):
        """Realiza la operación de Gauss sobre todas las matrices almacenadas.

        Returns:
            array: Resultados de las operaciones.
        """
        results = np.array([])
        for matrix in self.__matrices:
            result = self.checkMatrix(matrix)
            matrix = self.addToMatrix(matrix)
            np.set_printoptions(suppress=True, precision=3, floatmode='fixed')
            if result == "":
                result = validateGaussOperation(self, matrix)
            results = appendArray(results, result)
        return results
