class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        n = len(wordList)
        h = []
        def push(v):
            heapq.heappush(h,v)
        def pop():
            return heapq.heappop(h)
        push([0,beginWord])
        vis = set()
        while h:
            l = len(endWord)
            m = len(h)
            while m > 0:
                ans = pop()
                word = ans[1]
                if word == endWord:
                    return ans[0]+1
                if word not in vis:
                    vis.add(word)
                    for i in range(n):
                        dif = 0
                        x = wordList[i]
                        for j in range(l):
                            if word[j] != x[j]:
                                dif += 1
                            if dif > 1:
                                break
                        if dif == 1:
                            if x not in vis:
                                push([ans[0]+1,x])
                m -= 1
        return 0