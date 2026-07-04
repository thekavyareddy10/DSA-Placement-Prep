class Solution:
    def binaryToDecimal(self, b):

        result = 0
        power = len(b) - 1

        for digit in b:
            result = result + int(digit) * (2 ** power)
            power = power - 1

        return result