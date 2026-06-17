class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n + 1):
            count = 0
            num = i
            while num:
                count += num % 2
                num = num >> 1

            res.append(count)
        
        return res