class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        prefix = [0]*N
        postfix = [0]*N

        prefix[0] = 1
        postfix[N-1] = 1
        # populate prefix
        for i in range(1, N):
            prefix[i] = prefix[i - 1]*nums[i - 1]
        
        # populate postfix
        for i in range(N - 2, -1, -1):
            postfix[i] = postfix[i + 1]*nums[i + 1]

        res = [0]*N
        for i in range(N):
            res[i] = prefix[i] * postfix[i]

        return res
