class WordFilter:

    def __init__(self, words: List[str]):
        class Node:
            def __init__(self,index):
                self.children = [None] * 27
                self.index = index

        self.root = Node(0)
        def insert(string,index):
            n = len(string)
            s = string + '{' + string
            m = len(s)
            for i in range(n+1):
                curr = self.root
                for j in range(i,m):
                    w = s[j]
                    idx = ord(w) - ord('a')
                    if not curr.children[idx]:
                        curr.children[idx] = Node(index)
                        # curr.index = index
                    curr.children[idx].index = index
                    curr = curr.children[idx]

        for i,x in enumerate(words):
            insert(x,i)

        
    def f(self, pref: str, suff: str) -> int:
        curr = self.root
        word = suff + '{' + pref
        for x in word:
            idx = ord(x) - ord('a')
            if not curr.children[idx]:
                return -1
            curr = curr.children[idx]
        return curr.index

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)