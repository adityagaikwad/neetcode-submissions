class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        '''
        O(n log n)
        '''
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                # check if we can get consequtive nums in group
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        
        return True