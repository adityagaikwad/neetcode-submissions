"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Hash map two pass
        First pass creates map[oldNode] = newNode(oldNode.val)
        Second pass we add links
            map[oldNode].next = map[oldNode.next]
            map[oldNode].random = map[oldNode.random]

        Time: O(n)
        Space: O(n)
        '''

        '''
        Hash map one pass
        Time: O(n)
        Space: O(n)
        '''
        # oldToNew = defaultdict(lambda: Node(0))
        # # so that we do not end up creating a new node
        # # when curr.next or curr.random is None
        # oldToNew[None] = None

        # curr = head

        # while curr:
        #     # we create the node and assign val
        #     oldToNew[curr].val = curr.val
        #     # we create curr.next if not None
        #     # and when we come to the next node, we just add the value
        #     # same for random, we use the previously created Node ref
        #     # and assign value to it when curr gets to it
        #     oldToNew[curr].next = oldToNew[curr.next]
        #     oldToNew[curr].random = oldToNew[curr.random]

        #     curr = curr.next
        
        # return oldToNew[head]

        '''
        Space optimized three pass

        Time: O(n)
        Space: O(1)
        '''
        if not head:
            return None
        
        # add a copy node right after actual node
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        
        newHead = head.next
        
        # add references to random nodes for all duplicate nodes
        l1 = head
        while l1:
            l2 = l1.next
            if l1.random:
                # NOTE: = l1.random.next coz we need to point to copy
                # l1.random is original node .next is the copy
                l2.random = l1.random.next
            l1 = l2.next
        
        # separate the two lists
        l1 = head
        while l1:
            l2 = l1.next
            l1.next = l1.next.next
            if l2.next:
                l2.next = l2.next.next
            
            # l1.next is pointing to original node's next
            l1 = l1.next
        
        return newHead
