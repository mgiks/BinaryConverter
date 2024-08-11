class BinaryFloatingPointNumber():
    @staticmethod
    def mantissa(binary_mantissa):
        count = 0
        result = 0
        
        for bit in binary_mantissa:
            count += 1
            if bit == "1":
                result += 2**(-count)
                
        return result + 1
    
class CustomPrecision(BinaryFloatingPointNumber):
    @staticmethod
    def exponent(binary_exponent, count):
        bias_exponent = count
        result = 0
        
        for bit in binary_exponent:
            if bit == "1":
                result += 2**(count)
            count -= 1
            
        return result - 2**bias_exponent + 1

    @classmethod
    def decimal_number(cls, binary_number):
        binary_number = binary_number.strip()
        
        sign = 1 if binary_number[:1] else -1
        
        exponent_end = 2 
        
        for bit in binary_number[2:]:
            if bit == " ":
                break
            exponent_end += 1
        
        binary_length = len(binary_number[:exponent_end]) - 2 - 1
                
        exponent = cls.exponent(binary_number[2:exponent_end], binary_length)
        mantissa = cls.mantissa(binary_number[exponent_end + 1:])
        
        return (sign * mantissa * (2 ** exponent))

class SinglePrecision(BinaryFloatingPointNumber):
    @staticmethod
    def exponent(binary_exponent):
        count = 7
        bias_exponent = count
        result = 0
        
        for bit in binary_exponent:
            if bit == "1":
                result += 2**(count)
            count -= 1
            
        return result - 2**bias_exponent + 1

    @classmethod
    def decimal_number(cls, binary_number):
        binary_number = binary_number.replace(" ", "")
        
        sign = 1 if binary_number[:1] else -1
        exponent = cls.exponent(binary_number[1:9])
        mantissa = cls.mantissa(binary_number[9:])
        
        return (sign * mantissa * (2 ** exponent))

class DoublePrecision(BinaryFloatingPointNumber):
    @staticmethod
    def exponent(binary_exponent):
        count = 10
        bias_exponent = count
        result = 0
        
        for bit in binary_exponent:
            if bit == "1":
                result += 2**(count)
            count -= 1

        return result - 2**bias_exponent + 1
    
    @classmethod
    def decimal_number(cls, binary_number):
        binary_number = binary_number.replace(" ", "")
        
        sign = 1 if binary_number[:1] else -1
        exponent = cls.exponent(binary_number[1:12])
        mantissa = cls.mantissa(binary_number[12:])

        return (sign * mantissa * (2 ** exponent))
        
print(CustomPrecision.decimal_number("0 10000010 11101010101010101010101"))




