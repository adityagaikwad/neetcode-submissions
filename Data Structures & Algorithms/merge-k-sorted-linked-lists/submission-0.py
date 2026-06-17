# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        Iterative merge lists one by one approach
            Alternatively, can also find min of all lists
            and append and go to next min
        Time: O(n * k)
            where n is total number of nodes across k lists
        Space: O(1)
        '''
        # k = len(lists)

        # if k == 0:
        #     return None

        # for i in range(1, k):
        #     lists[i] = self.mergeLists(lists[i - 1], lists[i])
        
        # return lists[k - 1]

        '''
        Divide and conquer merge 2 lists
        i.e For k = 4
            Step 1 [Merge(0, 1), Merge(2, 3)]
            Step 2 [Merge(01, 23)]
            Step 3 if len = 1 return list
            and append and go to next min
        Time: O(n * k)
            where n is total number of nodes across k lists
        Space: O(1)
        '''
        k = len(lists)

        if k == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                mergedList = self.mergeLists(l1, l2)
                mergedLists.append(mergedList)
            lists = mergedLists

        return lists[-1]

    def mergeLists(self, l1, l2):
            if not l1:
                return l2
            
            if not l2:
                return l1

            res = curr = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                
                curr = curr.next
            
            curr.next = l1 if l1 else l2

            return res.next