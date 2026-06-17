class Node:
    def __init__(self):
        self.links = [None]*26
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord("a") - ord(ch)
            if not curr.links[index]:
                curr.links[index] = Node()
            
            curr = curr.links[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root        
        for ch in word:
            index = ord("a") - ord(ch)
            if not curr.links[index]:
                return False

            curr = curr.links[index]
        
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root        
        for ch in prefix:
            index = ord("a") - ord(ch)
            if not curr.links[index]:
                return False

            curr = curr.links[index]
        
        return True

        