class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        n = len(words)
        s = set(words)
        cache = {}
        def isValid(word,cnt):
            if (word,cnt) in cache:
                return cache[(word,cnt)]
            if not word and cnt > 1:
                # print(cnt)
                return True
            m = len(word)
            i = 0
            res = False
            # val = False
            for j in range(1,m+1):
                if word[:j] in s:
                    res = res or isValid(word[j:],cnt+1)
                    # print(res)
            cache[(word,cnt)] = res
            
            return res

        ans = []    
        for w in words:
            if isValid(w,0):
                ans.append(w)
        return ans