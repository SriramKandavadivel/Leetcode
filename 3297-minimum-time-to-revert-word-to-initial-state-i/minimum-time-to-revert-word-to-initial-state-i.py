class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        time = 0
        s = str(word) ###
        for i in range(0,n,k):
            f = s[0:k]
            s = s[k:]
            s = s+ f
            time += 1
            l = -1
            print(l)
            j = 0
            flag = True
            while l+1 < n-(i+k):
                # print(l)
                l+=1
                # print(l,j)
                if s[l] != word[j]:
                    flag = False
                    break
                j+=1
            if flag:
                return time
            
        return n//k