from collections import Counter
import heapq

class Solution:
    '''
    Min heap of size k to store top counts

    Time Complexity: O (n * log k)
    Space Complexity: O(n + k)

    n = len(nums)
    k = num of top frequent elements
    '''
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = {}
    #     for num in nums:
    #         count[num] = 1 + count.get(num, 0)
        
    #     heap = []
    #     for num in count.keys():
    #         heapq.heappush(heap, (count[num], num))

    #         if len(heap) > k:
    #             heapq.heappop(heap)
        
    #     res = []
    #     for i in range(k):
    #         res.append(heapq.heappop(heap)[1])
        
    #     return res

    '''
    Bucket sort approach. Build an arr called freq where freq[1] stores list of
    nums which have a frequency/count of 1 in nums and so on.

    Then go from freq[n] to lower till we get k nums of max freq.

    **Gotcha**: freq arr will be len (n + 1) coz freq can be 1 to n.

    Time Complexity: O(n)
    Space Complexity: O(n)

    n = len(nums)
    k = num of top frequent elements
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)

        # freq counts go from 1 to n. n when all nums are same
        freq = [[] for _ in range(n + 1)]

        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, count in counts.items():
            freq[count].append(num)
        
        i = n
        res = []
        while len(res) < k:
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    break
            
            i -= 1
        
        return res
            


