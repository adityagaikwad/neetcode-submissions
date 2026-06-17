class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}
        inDegrees = {c: 0 for c in adj}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            len1, len2 = len(w1), len(w2)
            minLen = min(len1, len2)

            # if prefix is same, first word len has to be < second word len
            # in valid scenario
            if len1 > len2 and w1[:minLen] == w2[:minLen]:
                return ""
            
            for j in range(minLen):
                # first mismatch gives lexicographical ordering
                if w1[j] != w2[j]:
                    # only add to adj and increase indegrees if 
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        inDegrees[w2[j]] += 1
                    # no need to check further letters
                    break
        
        queue = deque([c for c in inDegrees if inDegrees[c] == 0])
        res = []

        while queue:
            char = queue.popleft()
            res.append(char)
            for neighbor in adj[char]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        if len(res) != len(adj):
            return ""
        
        return "".join(res)