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

Time: O(max(m, n)) or O(m + n)
max(m, n) <= m + n <= 2 * max(m, n), so they're the same asymptotic complexity
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

'''
Traverse both lists simultaneously, summing digits with carry.
When one list is shorter, treat its missing digits as 0.
Each iteration produces one digit of the result (sum % 10)
and a carry (sum // 10) forwarded to the next position.
Handle any leftover carry after both lists are exhausted.

Time: O(m + n), Space: O(1)
'''
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
