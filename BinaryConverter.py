class BinaryFloatingPointNumber:
    
    @staticmethod
    def mantissa(binary_mantissa):
        count = 0
        result = 0

        for bit in binary_mantissa:
            count += 1
            if bit == "1":
                result += 2 ** (-count)

        return result + 1


class FloatCustomPrecision(BinaryFloatingPointNumber):

    @staticmethod
    def exponent(binary_exponent, count):
        bias_exponent = count
        result = 0

        for bit in binary_exponent:
            if bit == "1":
                result += 2 ** (count)
            count -= 1

        return result - 2**bias_exponent + 1

    @classmethod
    def to_decimal_number(cls, binary_number):
        binary_number = binary_number.strip()
        for i in range(len(binary_number)):
            if binary_number[i] not in ["0", "1"]:
                return f"Not a binary digit at the position {i}"

        sign = 1 if binary_number[:1] else -1

        exponent_end = 2

        for bit in binary_number[2:]:
            if bit == " ":
                break
            exponent_end += 1

        binary_length = len(binary_number[:exponent_end]) - 2 - 1

        exponent = cls.exponent(binary_number[2:exponent_end], binary_length)
        mantissa = cls.mantissa(binary_number[exponent_end + 1 :])

        return sign * mantissa * (2**exponent)


class FloatSinglePrecision(BinaryFloatingPointNumber):

    @staticmethod
    def exponent(binary_exponent):
        count = 7
        bias_exponent = count
        result = 0

        for bit in binary_exponent:
            if bit == "1":
                result += 2 ** (count)
            count -= 1

        return result - 2**bias_exponent + 1

    @classmethod
    def to_decimal_number(cls, binary_number):
        binary_number = binary_number.replace(" ", "")
        for i in range(len(binary_number)):
            if binary_number[i] not in ["0", "1"]:
                return f"Not a binary digit at the position {i}"

        sign = 1 if binary_number[:1] else -1
        exponent = cls.exponent(binary_number[1:9])
        mantissa = cls.mantissa(binary_number[9:])

        return sign * mantissa * (2**exponent)


class FloatDoublePrecision(BinaryFloatingPointNumber):

    @staticmethod
    def exponent(binary_exponent):
        count = 10
        bias_exponent = count
        result = 0

        for bit in binary_exponent:
            if bit == "1":
                result += 2 ** (count)
            count -= 1

        return result - 2**bias_exponent + 1

    @classmethod
    def to_decimal_number(cls, binary_number):
        binary_number = binary_number.replace(" ", "")
        for i in range(len(binary_number)):
            if binary_number[i] not in ["0", "1"]:
                return f"Not a binary digit at the position {i}"

        sign = 1 if binary_number[:1] else -1
        exponent = cls.exponent(binary_number[1:12])
        mantissa = cls.mantissa(binary_number[12:])

        return sign * mantissa * (2**exponent)


class UnsignedInteger:

    @staticmethod
    def to_decimal_number(binary_number):
        result = 0
        count = 0
        binary_number = binary_number.replace(" ", "")

        for i in range(len(binary_number) - 1, -1, -1):
            if binary_number[i] == "1":
                result += 2**count
            elif binary_number[i] == "0":
                pass
            else:
                return f"Not a binary digit at the position {i}"
            count += 1

        return result
