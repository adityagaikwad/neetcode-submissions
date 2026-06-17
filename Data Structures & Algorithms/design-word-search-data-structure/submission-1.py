'''
Time: O(n) for add and search
      n is the length of str passed to each function
Space: O(n + t)
       t is the total number of tries 
'''
class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord("a") - ord(ch)
            if not curr.children[index]:
                curr.children[index] = Node()
            
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(startFrom, root):
            curr = root

            for i in range(startFrom, len(word)):
                ch = word[i]
                if ch != ".":
                    index = ord("a") - ord(ch)
                    if not curr.children[index]:
                        return False
                    curr = curr.children[index]
                else:
                    for node in curr.children:
                        # if we get a valid word from any of the children
                        # return True
                        if node and dfs(i + 1, node):
                            return True
                    # if none of the children have the remaining word
                    # return False
                    return False
            
            return curr.isEnd

        return dfs(0, self.root)