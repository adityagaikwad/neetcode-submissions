# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode(0)
        carry = 0

        while l1 or l2:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            sumVal = n1 + n2 + carry
            # sum -> carry, val
            # 9   -> 0, 9
            # 12  -> 1, 2
            # 10  -> 1, 0
            carry = sumVal // 10
            sumVal = sumVal % 10

            curr.next = ListNode(sumVal)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        # we can also add carry to above while condition
        # while l1 or l2 or carry
        if carry:
            curr.next = ListNode(carry)

        return ans.next