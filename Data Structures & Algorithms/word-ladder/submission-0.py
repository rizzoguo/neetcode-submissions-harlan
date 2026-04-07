class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([beginWord])
        visit = set([beginWord])
        steps = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()

                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    for ch in 'abcdefghijklmnopqrstuvwxyz':
                        if ch == word[i]:
                            continue
                        newWord = word[:i] + ch + word[i + 1:]

                        if newWord in wordSet and newWord not in visit:
                            visit.add(newWord)
                            queue.append(newWord)
                
            steps += 1
        
        return 0