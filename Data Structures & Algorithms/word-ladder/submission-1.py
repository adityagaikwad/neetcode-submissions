'''
BFS solution

Time complexity: O(M^2 * N)
    M = length of word
    N = length of word list

    For each word in the list we make combo list -> (M x N) for "for" loop. 
    Then M time to create substring. (M^2 x N).

Space complexity: O(M^2 * N)
    combo_dict holds N * M pattern keys, each of length M.
    Queue and visited set hold at most N entries.
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (
            not beginWord
            or not endWord
            or not wordList
            or endWord not in wordList
            or beginWord == endWord
        ):
            return 0
        
        # intermediate_word_to_wordList_words_dict
        # key = intermediate word with one * (wildcard) char
        # value = list of possible words matching wildcard from wordList
        combo_dict = defaultdict(list)

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time
        for word in wordList:
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                combo_dict[intermediate_word].append(word)

        # IMP: start level = 1, beginWord is counted as one word in reaching endWord
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, level = queue.popleft()

            # Next states are all the words which share the same intermediate words
            for i in range(L):
                intermediate_word = word[:i] + "*" + word[i+1:]
                for nextWord in combo_dict[intermediate_word]:
                    if nextWord == endWord:
                        return level + 1
                    elif nextWord not in visited:
                        queue.append((nextWord, level + 1))
                        visited.add(nextWord)
        
        return 0

        