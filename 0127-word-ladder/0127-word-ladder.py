class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj = collections.defaultdict(list)
        for w in wordList:
            for j in range(len(w)):
                pattern = w[:j] + '*' + w[j+1:]
                adj[pattern].append(w)
        q = deque()
        q.append(beginWord)
        visit = set()
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                visit.add(word)
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + '*' + word[j+1:]
                    for nei in adj[pattern]:
                        if nei not in visit:
                            q.append(nei)
            res +=1  
        return 0
            


