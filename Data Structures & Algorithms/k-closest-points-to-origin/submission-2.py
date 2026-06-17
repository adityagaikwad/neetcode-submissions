'''
Need k closest points so use max heap of size k.
n - k larger distances will be removed from heap

Time: O(n log k)
Space: O(k)
'''
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            heapq.heappush(heap, (-self.dist(x, y), x, y))

            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]

    def dist(self, x, y):
        return x**2 + y**2

"""
Quick select approach

pivot < k  -> L = pivot + 1  -> go right
pivot > k  -> R = pivot - 1  -> go left
pivot == k -> stop

T.C. average O(n), worst O(n^2)
S.C. O(1)

quickselect partitions in-place until pivot index becomes k.
worst case happens when pivot choices are bad and the search area shrinks by only 1 each time.
"""
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         euclidean = lambda x: x[0]**2 + x[1]**2
        
#         def partition(left,right):
#             currentPivotsIndex = right
#             currentPivotsDistance = euclidean(points[currentPivotsIndex])

#             whereToPutPivotsIndexNextTime = left # will track the location we'll put pivot next

#             for curr in range(left,right):
#                 if euclidean(points[curr]) <= currentPivotsDistance:
#                     points[curr], points[whereToPutPivotsIndexNextTime] = points[whereToPutPivotsIndexNextTime], points[curr] #this is finding where to put our pivot at
#                     whereToPutPivotsIndexNextTime +=1

#             points[whereToPutPivotsIndexNextTime], points[right] = points[right], points[whereToPutPivotsIndexNextTime] #after finding so we locate now
#             return whereToPutPivotsIndexNextTime

#         left, right = 0, len(points) - 1
#         pivot = len(points) #make pivot idx impossible so while loop can always start

#         while pivot != k:
#             pivot = partition(left,right)

#             if pivot < k:
#                 left = pivot +1
#             else:
#                 right = pivot -1
#         return points[:k]

"""
IMPORTANT:
after each loop, we choose a NEW pivot.
each loop picks a fresh pivot from the current right boundary: points[R].
prev pivot position does not matter anymore.

arr = [3, 5, 7, 4, 1, 9], k = 3

GOAL:
pivot index should become k
pivot == 3 means first 3 nums are smallest enough

--------------------------------
ROUND 1
L = 0, R = 5
pivot value = 9

[3, 5, 7, 4, 1, 9]
 i              r

3 <= 9 yes -> i = 1
5 <= 9 yes -> i = 2
7 <= 9 yes -> i = 3
4 <= 9 yes -> i = 4
1 <= 9 yes -> i = 5

[3, 5, 7, 4, 1, 9]
                i/r

swap i,r -> same
pivot index = 5

pivot > k
5 > 3
R = pivot - 1 = 4

--------------------------------
ROUND 2
L = 0, R = 4
pivot value = 1

[3, 5, 7, 4, 1, 9]
 i           r

3 <= 1 no
5 <= 1 no
7 <= 1 no
4 <= 1 no

i stays 0

swap i,r:

[1, 5, 7, 4, 3, 9]
 ^
 pivot index = 0

pivot < k
0 < 3
L = pivot + 1 = 1

--------------------------------
ROUND 3
L = 1, R = 4
pivot value = 3

[1, 5, 7, 4, 3, 9]
    i        r

5 <= 3 no
7 <= 3 no
4 <= 3 no

i stays 1

swap i,r:

[1, 3, 7, 4, 5, 9]
    ^
    pivot index = 1

pivot < k
1 < 3
L = pivot + 1 = 2

--------------------------------
ROUND 4
L = 2, R = 4
pivot value = 5

[1, 3, 7, 4, 5, 9]
       i     r

7 <= 5 no
4 <= 5 yes -> swap i,j

[1, 3, 4, 7, 5, 9]
          i  r

swap i,r:

[1, 3, 4, 5, 7, 9]
          ^
          pivot index = 3

pivot == k
3 == 3
STOP

return arr[:3] = [1, 3, 4]
"""