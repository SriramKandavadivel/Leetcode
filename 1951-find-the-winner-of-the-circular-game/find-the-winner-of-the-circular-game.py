class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        # def josh(frnds, idx):
        #     if len(frnds) == 1:
        #         return frnds[0]
            
        #     idx = (idx + k) % len(frnds)

        #     frnds.pop(idx)

        #     return josh(frnds,idx)

        # k -=  1 # k-1 th position is to be deleted always
        # frnds = []
        # for i in range(n):
        #     frnds.append(i + 1)

        # return josh(frnds, 0)

        i = 1
        ans = 0
        while(i <= n):

            # update the value of ans
            ans = (ans + k) % i
            i += 1
        # returning the required answer
        return ans + 1