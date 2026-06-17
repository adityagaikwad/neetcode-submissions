class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start from least significant digit and add 1
        digits = digits[::-1]
        # we will start with remainder as 1 coz
        # we want to add 1 to the num anyways
        remainder = 1

        n = len(digits)
        i = 0
        while remainder:
            if i < n:
                if digits[i] == 9:
                    digits[i] = 0
                    remainder = 1
                else:
                    digits[i] += remainder
                    remainder = 0
            else:
                # remainder still exists at the end
                # of the digit iteration
                digits.append(1)
                remainder = 0
            i += 1
        
        return digits[::-1]