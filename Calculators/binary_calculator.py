class Binary:
    value = None
    one_complement = None
    two_complement = None

    def __init__(self, value: str) -> None:
        self.value = value

        # Calculate 1's complement
        temp_str = self.value.replace('0', '2')
        self.one_complement = temp_str.replace('1', '0').replace('2', '1')

        # Calculate 2's complement
        self.two_complement = BinaryMath.add_for_str(self.one_complement, '1')

    def get_value(self) -> str:
        return self.format_binary(self.value)

    def get_one_complement(self) -> str:
        return self.format_binary(self.one_complement)

    def get_two_complement(self) -> str:
        return self.format_binary(self.two_complement)

    def format_binary(self, binary_str) -> str:
        return binary_str[binary_str.find('1'):]

class BinaryMath:
    @staticmethod
    def add(num1:Binary, num2: Binary) -> Binary:
        return Binary(BinaryMath.add_for_str(num1.get_value(), num2.get_value()))

    @staticmethod
    def add_for_str(num1: str, num2: str) -> str:
        if not num1 or not num2:
            return ''

        maxlen = max(len(num1), len(num2))

        num1 = num1.zfill(maxlen)
        num2 = num2.zfill(maxlen)

        result  = ''
        carry   = 0

        i = maxlen - 1
        while(i >= 0):
            s = int(num1[i]) + int(num2[i])
            if s == 2: #1+1
                if carry == 0:
                    carry = 1
                    result = f'{result}{"0"}'
                else:
                    result = f'{result}{"1"}'
            elif s == 1: # 1+0
                if carry == 1:
                    result = f'{result}{"0"}'
                else:
                    result = f'{result}{"1"}'
            else: # 0+0
                if carry == 1:
                    result = f'{result}{"1"}'
                    carry = 0
                else:
                    result = f'{result}{"0"}'
            i = i - 1

        if carry > 0:
            result = f'{result}{"1"}'
        return result[::-1]

    @staticmethod
    def subtract(num1: Binary, num2: Binary) -> Binary:
        return Binary(BinaryMath.add(num1, Binary(num2.get_two_complement())).get_value()[1:])

# Test Code
testnum1 = Binary('10010')
testnum2 = Binary('00101')
print(BinaryMath.add(testnum1, testnum2).get_value())
