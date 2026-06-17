# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Recursion: check group exists, recurse on tail, then reverse this group
    Walk k steps to confirm a full group exists. If it does, recurse on the
    remainder so we get an already-reversed tail back as curr.
    Then reverse the current k nodes by repeatedly taking head (node 1, then
    node 2, ...) and prepending it in front of curr, which grows from the
    tail backwards. After k iterations, curr is the new head of this group.
    If fewer than k nodes remain, return head unchanged.

Time:  O(n)
Space: O(n/k)
    Each recursive call processes one group of k nodes, so the recursion depth 
    equals the number of groups, which is n/k. That depth is also the
    call stack size, so space is O(n/k)
'''
# class Solution:
#     def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         curr = head
#         group = 0

#         while curr and group < k:
#             curr = curr.next
#             group += 1
        
#         if group == k:
#             curr = self.reverseKGroup(curr, k)
#             while group > 0:
#                 tmp = head.next
#                 head.next = curr
#                 curr = head
#                 head = tmp
                
#                 group -= 1
            
#             head = curr
        
#         return head

'''
Iteration: locate kth node, reverse group in-place, stitch groups together
    Use a dummy node before head so every group always has a groupPrevEnd to
    attach to. Each pass through the loop handles one k-sized group:
      1. Move k steps from groupPrevEnd to find kthNode (becomes the new head
         of this group after reversal). If it doesn't exist, fewer than k
         nodes remain, so stop.
      2. Reverse the k nodes from groupPrevEnd.next through kthNode using a
         standard prev/curr reversal. Seed prev = groupNextStart so the tail
         of the reversed group already points to the next group automatically.
      3. Stitch: point groupPrevEnd to kthNode (the reversed group's new head),
         then advance groupPrevEnd to what was the group's first node, which is
         now the group's tail and the attachment point for the next group.

Time:  O(n)
Space: O(1)
'''
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
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
