'''
If we had merged the two arrays, then median would be middle of
left and right halfs of equal length. Both halfs will have parts of A and B sorted
arrays.
Ensure A is the smaller arr, else swap to make A smaller
A, B = B, A

Median = (rightmost num of left half + leftmost num of right half)/2 when len=even
else     leftmost of right half when len = odd

Because len(leftHalf) <= len(rightHalf) (< when odd and = when even)

For both arrs, we need to find the proper position of the partition such that
A[:ALeft + 1] + B[:BLeft + 1] form the final left partition if the two
arrs were merged and sorted completely. Same for right partition.

ALeft = rightmost idx of left partition contribution from arr A
ARight = leftmost idx of right partition contribution from arr A

BLeft = rightmost idx of left partition contribution from arr B
BRight = leftmost idx of right partition contribution from arr B

We use binary search to find the ALeft and ARight values on arr A
and since we know halfLen, BLeft = halfLen - ALeft
nums in A (left partition) = i = (l + r)//2
nums in B (left partition) = j = half - i - 2

Check if partition is valid: if ALeft <= BRight and BLeft <= ARight
When valid, median = 
if arrLen % 2 == 1:
    # since odd, min of ARight, BRight will be
    # leftmost element of second partition
    # i.e element at half + 1
    return min(ARight, BRight)
else:
    return max((ALeft, BLeft) + min(ARight, BRight)) / 2

Time: O(log min(m, n))
    Since we do binary search on smaller arr
Space: O(1)
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        arrLen = len(A) + len(B)
        halfLen = arrLen // 2
        
        # we use binary search to find the ALeft and ARight values
        # and since we know halfLen, BLeft = halfLen - ALeft
        # nums in A (left partition) = i = (l + r)//2
        # nums in B (left partition) = j = half - i - 2
        l, r = 0, len(A) - 1

        # there is a valid ans guranteed
        while True:
            # i represents the last index in A that is included in the left partition
            i = l + (r - l)//2

            # j is last index in B which is included in left partition starting from 0
            # hence (i + 1) + (j + 1) = half
            # hence j = half - i - 2
            j = halfLen - i - 2

            # confirm with claude why -inf and inf are defaults and add comments
            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if i + 1 < len(A) else float("inf")

            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if j + 1 < len(B) else float("inf")

            # check if partition is valid
            if ALeft <= BRight and BLeft <= ARight:
                if arrLen % 2 == 1:
                    # since odd, min of ARight, BRight will be
                    # leftmost element of second partition
                    # i.e element at half + 1
                    return min(ARight, BRight)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            # comparing ALeft coz binary search is on A
            elif ALeft > BRight:
                # More elements in A left partition than needed
                r = i - 1
            else:
                # else we need more elements in A left partition
                l = i + 1


