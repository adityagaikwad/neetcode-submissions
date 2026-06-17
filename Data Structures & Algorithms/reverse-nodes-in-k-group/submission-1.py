# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        Recursion
        Time: O(n)
        Space: O(n / √k)
        '''
        # curr = head
        # group = 0

        # while curr and group < k:
        #     curr = curr.next
        #     group += 1
        
        # if group == k:
        #     curr = self.reverseKGroup(curr, k)
        #     while group > 0:
        #         tmp = head.next
        #         head.next = curr
        #         curr = head
        #         head = tmp
                
        #         group -= 1
            
        #     head = curr
        
        # return head
        
        '''
        Iteration

        Time: O(n)
        Space: O(1)
        '''
        dummy = ListNode(0)
        dummy.next = head
        groupPrevEnd = dummy

        while True:
            # move k spaces ahead
            kthNode = self.moveKAhead(groupPrevEnd, k)
            # if we reach end, no need to sort last < k elements
            if not kthNode:
                break

            # next k nodes start pointer
            groupNextStart = kthNode.next

            # reverse from first to kthNode (including)
            # i.e groupEnd.next to one before groupStart (of next group)
            # prev = start of next group because we want in 1 2 3 4 5 6
            #  3 -> 2 -> 1 -> (6) -> 5 -> 4
            # i.e 1 points to 6
            prev = groupNextStart
            # we start from .next of prev group end
            curr = groupPrevEnd.next
            # reverse
            while curr != groupNextStart:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # make pointers to point from old group to new
            # first node of new group
            # eg. 3 -> 2 -> 1 (groupPrevEnd) -> (4 -> 5 -> 6) was before interation 2
            # then to make it  3 -> 2 -> 1 -> 6 -> 5 -> 4
            # we point 1 to 6 and then set groupPrevEnd to 4
            temp = groupPrevEnd.next
            groupPrevEnd.next = kthNode
            groupPrevEnd = temp

        return dummy.next

    def moveKAhead(self, node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node
