import numpy as np
from utils.helpers.arrays import appendArray
from utils.validations.operations import validateGaussOperation


class SeidelMatrixOp:
    """Clase para operaciones con matrices usando el método de Gauss-Seidel."""

    __matrices = np.array([])

    def __init__(self, mat):
        """Inicializa la clase SeidelMatrixOp.

        Args:
            mat (array): Arreglo de matrices a operar.

        Raises:
            ValueError: Si no se reciben matrices.
        """
        if len(mat) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = mat

    # Setters
    def setMatrix(self, matrix):
        """Establece las matrices a operar.

        Args:
            matrix (array): Arreglo de matrices.

        Raises:
            ValueError: Si no se reciben matrices o es None.
        """
        if matrix is None:
            raise ValueError("Error: Es necesario tener las matrices")
        elif len(matrix) == 0:
            raise ValueError("Error: No hay matrices")
        else:
            self.__matrices = matrix

    # Getters
    def getMatrix(self):
        """Devuelve las matrices almacenadas.

        Returns:
            array: Matrices almacenadas.
        """
        return self.__matrices

    # Métodos
    def operation(self, matrix, tol=1e-10, max_iter=1500):
        """Resuelve un sistema de ecuaciones lineales por el método de Gauss-Seidel.

        Args:
            matrix (array): Matriz aumentada del sistema.
            tol (float, optional): Tolerancia para la convergencia. Por defecto 1e-10.
            max_iter (int, optional): Número máximo de iteraciones. Por defecto 1500.

        Returns:
            array: Solución del sistema.

        Raises:
            ValueError: Si la matriz no es diagonalmente dominante o hay división por cero.
        """
        A = np.array(matrix, dtype=float)
        n = len(A)
        x = np.zeros(n)
        if not self.isDominant(A):
            A_new = self.convertDominant(A)
            if A_new is None:
                raise ValueError(
                    "No se pudo convertir la matriz a diagonalmente dominante")
            else:
                A = A_new
        for iteration in range(max_iter):
            x_old = x.copy()
            for i in range(n):
                if A[i, i] == 0:
                    raise ValueError(f"División por cero en la fila {i}")
                suma = 0.0
                for j in range(n):
                    if j != i:
                        suma += A[i, j] * x[j]
                x[i] = (A[i, -1] - suma) / A[i, i]
            diff = max(abs(x[i] - x_old[i]) for i in range(n))
            if diff < tol:
                break
        return x

    def isDominant(self, matrix):
        """Verifica si la matriz es diagonalmente dominante.

        Args:
            matrix (np.ndarray): Matriz a verificar.

        Returns:
            bool: True si es dominante, False en caso contrario.
        """
        n = len(matrix)
        for i in range(n):
            diag = abs(matrix[i][i])
            for j in range(n):
                if j != i:
                    if diag < abs(matrix[i][j]) or diag < abs(matrix[j][i]):
                        return False
        return True

    def convertDominant(self, matrix):
        """Convierte la matriz a una forma diagonalmente dominante si es posible.

        Args:
            matrix (np.ndarray): Matriz a convertir.

        Returns:
            np.ndarray: Matriz convertida.

        Raises:
            ValueError: Si no es posible convertir la matriz.
        """
        n = len(matrix)
        for i in range(n):
            maxVal = -1
            maxIndex = i
            for j in range(n):
                currentAbs = abs(matrix[i][j])
                if currentAbs > maxVal:
                    maxVal = currentAbs
                    maxIndex = j
            if maxIndex != i:
                matrix[[i, maxIndex]] = matrix[[maxIndex, i]]
        if not self.isDominant(matrix):
            raise ValueError(
                f"No es posible realizar esta operacion.")
        return matrix

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
        return len(self.__matrices)

    def checkMatrix(self, matrix):
        """Verifica si la matriz es cuadrada.

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
            return "Al no ser una matriz cuadrada, tendrá o infinitas soluciones o ninguna solución"
        return ""

    def startOperation(self):
        """Realiza la operación de Gauss-Seidel sobre todas las matrices almacenadas.

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