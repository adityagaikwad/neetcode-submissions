'''
Hashmap as trie node implementation
Time: (n) for each call
      n = len(string)
Space: O(t)
       t = len(total trieNodes created)
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

'''
Static 26 char arr implementation
'''
# class Node:
#     def __init__(self):
#         self.links = [None]*26
#         self.isEnd = False

# class PrefixTree:

#     def __init__(self):
#         self.root = Node()

#     def insert(self, word: str) -> None:
#         curr = self.root
#         for ch in word:
#             index = ord("a") - ord(ch)
#             if not curr.links[index]:
#                 curr.links[index] = Node()
            
#             curr = curr.links[index]
#         curr.isEnd = True

#     def search(self, word: str) -> bool:
#         curr = self.root        
#         for ch in word:
#             index = ord("a") - ord(ch)
#             if not curr.links[index]:
#                 return False

#             curr = curr.links[index]
        
#         return curr.isEnd

#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root        
#         for ch in prefix:
#             index = ord("a") - ord(ch)
#             if not curr.links[index]:
#                 return False

#             curr = curr.links[index]
        
#         return True
