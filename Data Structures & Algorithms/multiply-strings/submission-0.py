class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either number is "0", return "0"
        if "0" in [num1, num2]:
            return "0"

        # Result can be at most len(num1) + len(num2) digits
        res = [0] * (len(num1) + len(num2))

        # Reverse both strings for easier indexing from least significant digit
        num1, num2 = num1[::-1], num2[::-1]

        # Multiply each digit and store the result at corresponding position
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])  # Multiply digits
                res[i1 + i2] += digit  # Add to position (carry handled next)
                res[i1 + i2 + 1] += res[i1 + i2] // 10  # Carry to next digit
                res[i1 + i2] %= 10  # Keep only unit place

        # Reverse result to correct order and remove leading zeros
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1

        # Convert digits to string and join
        res = map(str, res[beg:])
        return "".join(res)