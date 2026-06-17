class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        arrSum = len(A) + len(B)
        half = arrSum//2

        # we use A(smaller arr) to find the optimum nums in both Arr
        # nums in A (left partition) = i = (l + r)//2
        # nums in B (left partition) = j = half - i - 2
        l, r = 0, len(A) - 1

        # there is a valid ans guranteed
        while True:
            # i represents the last index in A that is included in the left partition
            i = (l + r)//2
            # j is last index in B which is included in left partition starting from 0
            # hence (i + 1) + (j + 1) = half
            # hence j = half - i - 2
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float("-inf")
            ARight = A[i + 1] if i < len(A) - 1 else float("inf")
            
            BLeft = B[j] if j >= 0 else float("-inf")
            BRight = B[j + 1] if j < len(B) - 1 else float("inf")

            # check if partition is valid
            if ALeft <= BRight and BLeft <= ARight:
                # find median
                if arrSum % 2 == 1:
                    # since odd, min of ARight, BRight will be
                    # leftmost element of second partition
                    # i.e element at half + 1
                    return min(ARight, BRight)
                else:
                    # rightmost of left partition + leftmost of right partition /2
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2
            elif ALeft > BRight:
                # More elements in A left partition than needed
                r = i - 1
            else:
                # else we need more elements in A left partition
                l = i + 1
    
