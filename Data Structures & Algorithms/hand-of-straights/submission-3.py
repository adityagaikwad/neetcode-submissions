'''
Time: O(n log n)
    n = len(hand)
    g = groupSize
    nlogn for sort, then max n for the for loop

Space: O(n) for counter
'''
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize:
            return False
        
        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                # check if we can get consequtive nums in group
                for i in range(num, num + groupSize):
                    # not possible to form a consecutive num group anymore
                    if not count[i]:
                        return False
                    count[i] -= 1
        
        return True

'''
Time: O(n * g) (can be worse) and may not work for all cases
    g is group size, n is total nums
'''
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize:
#             return False

#         count = Counter(hand)
#         for num in hand:
#             start = num
#             # The while count[start - 1] makes sure you always go back
#             # to the earliest possible start of a valid group.
#             while count[start - 1]:
#                 start -= 1

#             # we found the smallest number, and know that all nums
#             # from start to "num" exist in the arr. So these are all
#             # valid smaller nums to find groups for
#             while start <= num:
#                 if count[start]:
#                     for i in range(start, start + groupSize):
#                         if not count[i]:
#                             return False
#                         count[i] -= 1
#                     # check for group from next num
#                 start += 1
#         return True