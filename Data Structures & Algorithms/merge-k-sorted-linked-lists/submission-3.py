# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Approach: sequential pairwise merge
    Merge lists[0] into lists[1], then that result into lists[2],
    and so on until one fully merged list remains at lists[k-1].
    mergeLists() does a standard two-pointer merge of two sorted lists.

Time:  O(n * k)  -- each of the k merges touches progressively more nodes;
                    the total work sums to O(n/k * (2+3+...+k)) = O(nk)
Space: O(1)      -- rewires existing nodes, no extra allocations
'''
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        k = len(lists)

        if k == 0:
            return None

        # each iteration merges the accumulated result (lists[i-1]) with the
        # next list, storing the merged head back into lists[i]
        for i in range(1, k):
            lists[i] = self.mergeLists(lists[i - 1], lists[i])

        # after the loop, lists[k-1] holds the final fully merged list
        return lists[k - 1]

    def mergeLists(self, l1, l2):
            if not l1:
                return l2

            if not l2:
                return l1

            # dummy head so we never have to special-case the first node
            res = curr = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next

                curr = curr.next

            # at most one list still has nodes; attach the remainder directly
            curr.next = l1 if l1 else l2

            # skip the dummy head
            return res.next

'''
Divide and conquer merge 2 lists
i.e For k = 4
    Step 1 [Merge(0, 1), Merge(2, 3)]
    Step 2 [Merge(01, 23)]
    Step 3 if len = 1 return list
    and append and go to next min
Time: O(n * logk)
    Since we have k lists first time, then k/2, then k/4 etc
    And at each merge step all N nodes are processed
    Hence n * log(k)
    
    where n is total number of nodes across k lists
Space: O(1)
'''
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None
        
#         # when only one left that means last round of divide and conquer is over
#         while len(lists) > 1:
#             mergedLists = []
#             for i in range(0, len(lists), 2):
#                 l1 = lists[i]
#                 l2 = lists[i + 1] if i + 1 < len(lists) else None
#                 mergedList = self.mergeLists(l1, l2)
#                 mergedLists.append(mergedList)
#             # put mergedLists back into lists for
#             # next round of divide and conquer
#             lists = mergedLists

#         return lists[-1]

#     def mergeLists(self, l1, l2):
#             if not l1:
#                 return l2
            
#             if not l2:
#                 return l1

#             res = curr = ListNode(0)
#             while l1 and l2:
#                 if l1.val < l2.val:
#                     curr.next = l1
#                     l1 = l1.next
#                 else:
#                     curr.next = l2
#                     l2 = l2.next
                
#                 curr = curr.next
            
#             curr.next = l1 if l1 else l2

#             return res.next

'''
Min Heap solution

Add first node from each LL to the heap with a custom iterator (__lt__)

Then while len(minHeap) > 0, pop smallest and do curr.next = smallest
then add smallest.next back to the heap if not None

Time: O(n * logk)
        where n is total number of nodes across k lists
Space: O(k)
'''
# Added code
class Node:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        minHeap = []

        # add first elements of all lists to heap
        for l in lists:
            if l:
                heapq.heappush(minHeap, Node(l))
        
        ans = curr = ListNode(0)

        while len(minHeap) > 0:
            minNode = heapq.heappop(minHeap)
            listNode = minNode.node

            curr.next = listNode
            curr = curr.next
            listNode = listNode.next

            if listNode:
                heapq.heappush(minHeap, Node(listNode))
        
        return ans.next
