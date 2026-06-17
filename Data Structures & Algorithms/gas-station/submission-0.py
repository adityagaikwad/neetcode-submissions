class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        O(n^2) solution
        '''
        # n = len(gas)

        # for i in range(n):
        #     tank = gas[i] - cost[i]
        #     if tank < 0:
        #         continue

        #     j = (i + 1) % n
        #     while j != i:
        #         tank += gas[j]
        #         tank -= cost[j]
        #         if tank < 0:
        #             break
        #         j += 1
        #         j %= n

        #     if j == i:
        #         return i
        # return -1

        '''
        O(n) greedy solution
        Check if sum(gas) >= sum(cost), if yes only then can we complete a loop
        else return -1

        start from left and get total diff starting from i=0
        whenever we get total < 0 reset starting to next idx
        coz if total is <0 at some point, we cannot proceed.

        when we first reach end with positive total,
        the first idx we have rn is the ans. We do not need to go 
        to prev elements coz sum(gas) >= sum(cost) so prev stations
        can definitely be visited
        '''

        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                # curr gas station makes total < 0, start again from next idx
                start = i + 1

        return start