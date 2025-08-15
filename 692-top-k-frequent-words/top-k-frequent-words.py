class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = Counter(words)
        # print(d)


        ans = sorted(d, key = lambda k: (-d[k], k))
        # print(ans)
        return ans[:k]
            
    