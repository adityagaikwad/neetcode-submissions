# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode(0)
        remainder = 0

        while l1 and l2:
            n1 = l1.val
            n2 = l2.val

            sumVal = n1 + n2 + remainder
            # 9 -> 0, 9
            # 12 -> 1, 2
            # 10 -> 1, 0
            remainder = sumVal // 10
            if remainder:
                sumVal = sumVal % 10

            curr.next = ListNode(sumVal)

            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        node = l1 if l1 else l2
        
        while node:
            sumVal = node.val + remainder
            remainder = sumVal // 10
            if remainder:
                sumVal = sumVal % 10

            curr.next = ListNode(sumVal)

            node = node.next
            curr = curr.next

        if remainder:
            curr.next = ListNode(remainder)

        return ans.next