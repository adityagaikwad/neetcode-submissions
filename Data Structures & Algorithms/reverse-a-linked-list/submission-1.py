# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Iterative

curr → the current node we are processing
prev → the node that should come after curr once reversed
temp → the original next node (so we don't break the chain)
By moving these pointers forward in each step, we gradually reverse the entire list.
When curr becomes null, the list is fully reversed, and prev points to the new head.

Time: O(n)
Space: O(1)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

'''
Recursive reversal: recurse to the end of the list, then re-wire
pointers on the way back up.

Base case: empty list or single node — already reversed, return as-is.

Recursive case: assume reverseList(head.next) fully reverses the rest
of the list and returns its new head. At that point head.next still
points to what is now the TAIL of the reversed sublist. Wire that tail
back to head, then sever head.next to avoid a cycle.

Example: 1 -> 2 -> 3 -> None

    recurse down to 3 (base case), returns newHead = 3
    back at 2: 2.next (which is 3) points back to 2  ->  3 -> 2
                sever 2.next = None                   ->  3 -> 2 -> None
    back at 1: 1.next (which is 2) points back to 1  ->  3 -> 2 -> 1
                sever 1.next = None                   ->  3 -> 2 -> 1 -> None

    return newHead = 3 all the way up.

Time: O(n), Space: O(n) call stack
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            # so the next node points back to the current node
            head.next.next = head
        
        # to avoid cycles
        head.next = None

        # return the new head returned by the deepest recursive call
        return newHead




