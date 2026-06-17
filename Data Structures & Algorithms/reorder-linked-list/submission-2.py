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
        # nodes = []
        # curr = head

        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # i = 0
        # j = len(nodes) - 1

        # while i < j:
        #     nodes[i].next = nodes[j]
        #     i += 1

        #     # for odd numbers, we only add i value and break
        #     if i >= j:
        #         break
            
        #     nodes[j].next = nodes[i]
        #     j -= 1
        
        # # break the old pointer for the middle num/node, its now the end
        # nodes[i].next = None

        '''
        Two pointers

        Time complexity: O(n)
        Space complexity: O(n)
        '''

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # when fast reaches last node, slow reaches mid way
        # i.e at n/2 which is the start of second half
        # since the return value is [0, n - 1, ....]
        # it will be the last value in the arr
        # we can reverse the list from n/2 + 1 ... -> n -1
        # to be n - 1 -> ... n/2 + 1. Making it easier to do
        # [0, n - 1, ....] by taking one values from both lists

        # we now reverse this list starting at slow + 1
        curr = slow.next
        # the other list will end at current slow.next
        prev = slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # list is reversed and head is at prev
        first, second = head, prev

        # since second starts second half of the list, its len
        # will always be <= len(first half). For odd len [1,2,3,4,5]
        # slow/mid will be at 3 so second starts at 4
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
