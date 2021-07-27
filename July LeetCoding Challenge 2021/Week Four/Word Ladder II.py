class Solution:
    def findLadders(self, begW, endW, wordList):
        wordList += [begW]
        n, k = len(wordList), len(wordList[0])
        patterns = defaultdict(set)
        for word in wordList:
            for ind in range(0, k):
                tmp = word[0:ind] + "*" + word[ind+1:]
                patterns[tmp].add(word)
                
        G = defaultdict(set)
        for elem in patterns.values():
            for x, y in permutations(elem, 2):
                G[x].add(y)
                
        deps = {w: -1 for w in wordList}
        deps[begW] = 0
        paths = defaultdict(list)
        paths[begW] = [[begW]]
        queue = deque([begW])

        while queue:
            w = queue.popleft()
            if w == endW: return paths[w]
            for neib in G[w]:
                if deps[neib] == -1 or deps[neib] == deps[w] + 1:
                    if deps[neib] == -1:
                        queue.append(neib)
                        deps[neib] = deps[w] + 1
                    for elem in paths[w]:
                        paths[neib].append(elem + [neib])
