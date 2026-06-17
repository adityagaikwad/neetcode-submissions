class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        O(n log n)
        '''
        res = []
        for num in range(n + 1):
            count = 0
            while num:
                count += num % 2
                # right shift happens logn times with base 2
                num = num >> 1

            res.append(count)
        
        return res

        '''
        DP
        Count of prev nums repeat every 1,2,4,8,16... numbers
        '''
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp