# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Brute force is add nodes to list and access
        nodes[n - 1] and set nodes[n-1].next = nodes[n].next
        
        O(N) complexities
        '''

        '''
        Two pass

        Count total in one pass, then shift right by total - n
        then curr.next = curr.next.next
        Time: O(N)
        Space: O(1)
        '''
        # listLen = 0

        # node = head
        # while node:
        #     listLen += 1
        #     node = node.next
        
        # if n > listLen:
        #     return None

        # posFromStart = listLen - n

        # if posFromStart == 0:
        #     return head.next
    
        # prev = None
        # curr = head
        # nextN = curr.next

        # # iterate to pos - 1
        # for i in range(listLen - 1):
        #     if i + 1 == posFromStart:
        #         # curr is at one before removal node
        #         curr.next = curr.next.next
        #         break
        #     curr = curr.next

        # return head

        '''
        Two pointers, one pass

        Keep left and right pointers n nodes apart.
        Move right to position n from head, then advance both
        until right falls off the end. At that point left is sitting
        one before the node to remove, so skip it with left.next = left.next.next.

        Time: O(N)
        Space: O(1)
        '''
        dummy = ListNode(0, head)
        # start left one node before head
        left = dummy
        right = head
        # move right ahead by n
        while n > 0:
            right = right.next
            n -= 1
        
        # then we move right ahead till N (total len)
        # i.e ahead by N - n
        # therefore left is now at N - (n + 1)
        # i.e one before the node to be removed
        while right:
            left = left.next
            right = right.next
        
        # since left is one node before the node to be removed
        # we skip left.next(i.e node to be removed) to equal
        # left.next.next
        left.next = left.next.next

        return dummy.next





