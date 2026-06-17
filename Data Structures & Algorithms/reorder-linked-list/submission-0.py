# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        Brute force

        Time complexity: O(n)
        Space complexity: O(n)
        '''
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        i = 0
        j = len(nodes) - 1

        while i < j:
            nodes[i].next = nodes[j]
            i += 1

            # for odd numbers, we only add i value and break
            if i >= j:
                break
            
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None


