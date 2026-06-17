# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Iterate l1 and l2 and calculate total = l1 + l2 + remainder
Then currDigit = total % 10
     remainder = total // 10

Then for leftover digits of l1 or l2 whichever is longer do the same
And add remainder to next node if it still exists

Time: O(n)
Space: O(1)
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        remainder = 0
        dummy = curr = ListNode(0)

        while l1 and l2:
            total = l1.val + l2.val + remainder
            
            curr.next = ListNode(total % 10)
            remainder = total // 10

            l1 = l1.next
            l2 = l2.next
            curr = curr.next
        
        while l1:
            total = l1.val + remainder
            curr.next = ListNode(total % 10)
            remainder = total // 10
            l1 = l1.next
            curr = curr.next

        while l2:
            total = l2.val + remainder
            curr.next = ListNode(total % 10)
            remainder = total // 10
            l2 = l2.next
            curr = curr.next
        
        if remainder:
            curr.next = ListNode(remainder)

        return dummy.next

