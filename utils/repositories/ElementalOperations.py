import numpy as np
from array import ArrayType


class ElementalOperations:
    """Representación de las operaciones elementales.

    Attributes:
        number (str): Número a evaluar.
        base (ArrayType[str]): Base de las operaciones.
        operations (str): Operaciones a realizar.
    """

    __number = "0"
    __base = np.array([])
    __operations = ""

    def __init__(self, number: str = "0", base: ArrayType[str] = np.array([])):
        if len(number) == 0:
            raise Exception("Manage-Error: El numero no puede estar vacio")
        self.__number = self.__utilNumber(number)
        self.__base = base

    def setNumber(self, number: str) -> None:
        """Establece el número.

        Args:
            number (str): Número a evaluar.
        """
        if len(number) == 0:
            raise Exception("Manage-Error: El numero no puede estar vacio")
        self.__number = self.__utilNumber(number)

    def getNumber(self) -> str:
        """Devuelve el número.

        Returns:
            str: Número a evaluar.
        """
        return self.__number

    def setBases(self, base: ArrayType[str]) -> None:
        """Establece las bases de las operaciones.

        Args:
            base (ArrayType[str]): Base de las operaciones.
        """
        self.__base = base

    def getBases(self) -> ArrayType[str]:
        """Devuelve las bases de las operaciones.

        Returns:
            ArrayType[str]: Base de las operaciones.
        """
        return self.__base

    def getOperations(self) -> str:
        """Devuelve las operaciones a realizar.

        Returns:
            str: Operaciones a realizar.
        """
        self.__doOperations()
        return self.__operations

    def __decimalSum(self, a: str, b: str = "2"):
        """Suma decimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la suma.
        """
        # Permitir float si hay '.'
        if '.' in a or '.' in b:
            a = float(a)
            b = float(b)
            result = a + b
            return str(result)
        else:
            a = int(a)
            b = int(b)
            current = a
            result = a
            for _ in range(b):
                current += 1
                result = current
            return str(result)


    def __decimalSubs(self, a: str, b: str = "2"):
        """Resta decimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la resta.
        """
        # Permitir float si hay '.'
        if '.' in a or '.' in b:
            a = float(a)
            b = float(b)
            result = a - b
            return str(result)
        else:
            a = int(a)
            b = int(b)
            if a >= b:
                current = b
                result = a
                for _ in range(b):
                    current += 1
                    result -= 1
                return str(a - b)
            else:
                current = a
                result = b
                for _ in range(a):
                    current += 1
                    result -= 1
                return str(b - a)


    def __decimalMult(self, a: str, b: str = "2"):
        """Multiplica decimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la multiplicación.
        """
        # Permitir float si hay '.'
        if '.' in a or '.' in b:
            a = float(a)
            b = float(b)
            result = a * b
            return str(result)
        else:
            result = "0"
            for i, digit in enumerate(reversed(b)):
                partial = "0"
                for _ in range(int(digit)):
                    partial = self.__decimalSum(partial, a)
                result = self.__decimalSum(result, partial + "0" * i)
            return result

    def __decimalDiv(self, a: str, b: str = "2"):
        """Divide decimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la división.
        """
        a = a.lstrip("0") or "0"
        b = b.lstrip("0") or "0"
        # Permitir float si hay '.'
        if '.' in a or '.' in b:
            a_f = float(a)
            b_f = float(b)
            if b_f == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = a_f / b_f
            return str(result), "0"
        else:
            if b == "0":
                raise ZeroDivisionError("Cannot divide by zero")
            if a == "0":
                return "0"
            quotient = ""
            current_pos = 0
            remainder = ""
            while current_pos < len(a):
                remainder += a[current_pos]
                current_pos += 1
                remainder = remainder.lstrip("0") or "0"
                if len(remainder) < len(b) or (len(remainder) == len(b) and remainder < b):
                    quotient += "0"
                    continue
                count = 0
                while len(remainder) > len(b) or (
                    len(remainder) == len(b) and remainder >= b
                ):
                    remainder = self.__decimalSubs(remainder, b)
                    count += 1
                    remainder = remainder.lstrip("0") or "0"
                quotient += str(count)
            return quotient.lstrip("0") or "0", remainder.lstrip("0") or "0"

    def __binarySum(self, a: str, b: str = "10"):
        """Suma binarias.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "10".

        Returns:
            str: Resultado de la suma.
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = 0
        result = ""
        for i in range(max_len - 1, -1, -1):
            total = carry + (1 if a[i] == "1" else 0) + (1 if b[i] == "1" else 0)
            result = ("1" if total % 2 == 1 else "0") + result
            carry = total // 2
        if carry:
            result = "1" + result
        return result

    def __binarySubs(self, a: str, b: str = "10"):
        """Resta binarias.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "10".

        Returns:
            str: Resultado de la resta.
        """
        a_clean = a.lstrip("0") or "0"
        b_clean = b.lstrip("0") or "0"

        if len(a_clean) > len(b_clean):
            larger, smaller = a, b
        elif len(a_clean) < len(b_clean):
            larger, smaller = b, a
        else:
            for bit_a, bit_b in zip(a_clean, b_clean):
                if bit_a > bit_b:
                    larger, smaller = a, b
                    break
                elif bit_b > bit_a:
                    larger, smaller = b, a
                    break
            else:
                return "0"

        max_len = max(len(larger), len(smaller))
        larger = larger.zfill(max_len)
        smaller = smaller.zfill(max_len)

        result = ""
        borrow = 0

        for i in range(max_len - 1, -1, -1):
            bit_larger = int(larger[i])
            bit_smaller = int(smaller[i])

            diff = bit_larger - bit_smaller - borrow

            if diff < 0:
                diff += 2
                borrow = 1
            else:
                borrow = 0

            result = str(diff) + result

        result_str = result.lstrip("0")
        return result_str if result_str else "0"

    def __binaryMult(self, a: str, b: str = "10"):
        """Multiplica binarias.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "10".

        Returns:
            str: Resultado de la multiplicación.
        """
        result = "0"
        b_len = len(b)

        for i in range(b_len):
            if b[b_len - 1 - i] == "1":
                result = self.__binarySum(result, a + "0" * i)

        return result

    def __binaryDiv(self, a: str, b: str = "10"):
        """Divide binarias.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "10".

        Returns:
            str: Resultado de la división.
        """
        if b == "0":
            raise ValueError("Cannot divide by zero.")

        quotient = ""
        remainder = a

        while len(remainder) >= len(b):
            temp_divisor = b + "0" * (len(remainder) - len(b))
            if remainder >= temp_divisor:
                remainder = self.__binarySubs(remainder, temp_divisor)
                quotient += "1"
            else:
                quotient += "0"

        return quotient.lstrip("0") or "0", remainder

    def __hexSum(self, a: str, b: str = "2"):
        """Suma hexadecimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la suma.
        """
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)[-max_len:]
        b = b.zfill(max_len)[-max_len:]

        result = ""
        carry = 0
        hex_digits = "0123456789abcdef"

        for i in range(max_len - 1, -1, -1):
            digit_a = hex_digits.index(a[i])
            digit_b = hex_digits.index(b[i])

            total = digit_a + digit_b + carry
            carry = total // 16
            result = hex_digits[total % 16] + result

        if carry:
            result = hex_digits[carry] + result

        return result

    def __hexSubs(self, a: str, b: str = "2"):
        """Resta hexadecimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la resta.
        """
        if len(a) > len(b):
            larger, smaller = a, b
        elif len(a) < len(b):
            larger, smaller = b, a
        else:
            for d_a, d_b in zip(a, b):
                if d_a > d_b:
                    larger, smaller = a, b
                    break
                elif d_b > d_a:
                    larger, smaller = b, a
                    break
            else:
                return "0"

        max_len = max(len(larger), len(smaller))
        larger = larger.zfill(max_len)
        smaller = smaller.zfill(max_len)
        result = ""
        borrow = 0
        hex_digits = "0123456789abcdef"

        for i in range(max_len - 1, -1, -1):
            digit_l = larger[i]
            digit_s = smaller[i]
            value_l = hex_digits.index(digit_l)
            value_s = hex_digits.index(digit_s)

            diff = value_l - value_s - borrow
            if diff < 0:
                diff += 16
                borrow = 1
            else:
                borrow = 0

            result = hex_digits[diff] + result

        result_str = result.lstrip("0")
        return result_str if result_str else "0"

    def __hexMult(self, a: str, b: str = "2"):
        """Multiplica hexadecimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la multiplicación.
        """
        if a == "0" or b == "0":
            return "0"

        hex_digits = "0123456789abcdef"
        result = "0"

        for i, digit in enumerate(reversed(b)):
            digit_val = hex_digits.index(digit)
            partial_result = []
            carry = 0

            for d in reversed(a):
                product = (digit_val * hex_digits.index(d)) + carry
                carry = product // 16
                partial_result.append(hex_digits[product % 16])

            if carry:
                partial_result.append(hex_digits[carry])

            partial_result.reverse()
            partial_result_str = "".join(partial_result) + "0" * i
            result = self.__hexSum(result, partial_result_str)

        return result

    def __hexDiv(self, a: str, b: str = "2"):
        """Divide hexadecimales.

        Args:
            a (str): Primer número.
            b (str, optional): Segundo número. Defaults to "2".

        Returns:
            str: Resultado de la división.
        """
        a = a.lower().lstrip("0") or "0"
        b = b.lower().lstrip("0") or "0"

        if b == "0":
            raise ZeroDivisionError("Division by zero")

        if a == "0":
            return ("0", "0")

        quotient = ""
        current_pos = 0
        remainder = ""
        hex_digits = "0123456789abcdef"

        while current_pos < len(a):
            remainder += a[current_pos]
            current_pos += 1

            remainder = remainder.lstrip("0") or "0"

            if len(remainder) < len(b) or (len(remainder) == len(b) and remainder < b):
                quotient += "0"
                continue

            count = 0
            while len(remainder) > len(b) or (
                len(remainder) == len(b) and remainder >= b
            ):
                remainder = self.__hexSubs(remainder, b)
                count += 1
                remainder = remainder.lstrip("0") or "0"

            quotient += hex_digits[count]

        return (quotient.lstrip("0") or "0", remainder.lstrip("0") or "0")

    def __decimalOperations(self, op: str):
        """Devuelve las operaciones decimales.

        Args:
            op (str): Operaciones a realizar.

        Returns:
            str: Operaciones a realizar.
        """
        op += " dec:"
        n = self.__decimalSum(self.__number)
        op += "+;"
        n = self.__decimalSubs(self.__number)
        op += "-;"
        n = self.__decimalMult(self.__number)
        op += "*;"
        n = self.__decimalDiv(self.__number)
        op += "/;"
        return op

    def __binaryOperations(self, op: str):
        """Devuelve las operaciones binarias.

        Args:
            op (str): Operaciones a realizar.

        Returns:
            str: Operaciones a realizar.
        """
        op += " bin:"
        n = self.__binarySum(self.__number)
        op += "+;"
        n = self.__binarySubs(self.__number)
        op += "-;"
        n = self.__binaryMult(self.__number)
        op += "*;"
        n, m = self.__binaryDiv(self.__number)
        op += "/;"
        return op

    def __hexOperations(self, op: str):
        """Devuelve las operaciones hexadecimales.

        Args:
            op (str): Operaciones a realizar.

        Returns:
            str: Operaciones a realizar.
        """
        op += " hex:"
        n = self.__hexSum(self.__number)
        op += "+;"
        n = self.__hexSubs(self.__number)
        op += "-;"
        n = self.__hexMult(self.__number)
        op += "*;"
        n, m = self.__hexDiv(self.__number)
        op += "/;"
        return op

    def __doOperations(self) -> None:
        """Realiza las operaciones.

        Returns:
            None
        """
        self.__operations = ""
        self.__number = self.__number.lower().replace(",", ".")
        self.__number = self.__number.split(".")[0]
        for operation in self.__base:
            if operation == "Decimal":
                # self.__operations = self.__decimalOperations(self.__operations)
                self.__operations += " dec:+;-;*;/;"
            elif operation == "Binario":
                # self.__operations = self.__binaryOperations(self.__operations)
                self.__operations += " bin:+;-;*;/;"
            elif operation == "Hexadecimal":
                # self.__operations = self.__hexOperations(self.__operations)
                self.__operations += " hex:+;-;*;/;"
            else:
                raise Exception("Manage-Error: Operacion no valida")
        self.__operations = self.__operations.rstrip(";")
        self.__operations = self.__operations.lstrip()

        if len(self.__operations) == 0:
            self.__operations = "No hay operaciones disponibles"

    def __utilNumber(self, number: str):
        """Valida el número ingresado.

        Args:
            number (str): Número a validar.

        Returns:
            str: Número validado.

        Raises:
            Exception: Si el número no es válido.
        """
        chars_allowed = "-0123456789ABCDEF.,"
        for char in number:
            if char.upper() not in chars_allowed:
                raise Exception("Manage-Error: El numero ingresado no es valido")
        if number.startswith((".", ",")) or number.endswith((".", ",")):
            raise Exception("Manage-Error: El numero ingresado no es valido")
        separatorCount = number.count(".") + number.count(",")
        if separatorCount > 1:
            raise Exception("Manage-Error: El numero ingresado no es valido")
        if number == "0":
            return "0"
        else:
            return number.lstrip("0")