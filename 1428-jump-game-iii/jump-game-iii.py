class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        vis= {}
        def rec(idx):
            if idx >= n or idx < 0:
                return False
            if idx in vis:
                return False
            if arr[idx] == 0:
                return True
            # if idx == n-1 :
            #     vis[idx] = True 
            # if idx == 0:
            vis[idx] = True
            flag = False
            flag = rec(idx+arr[idx]) or flag
            flag = rec(idx-arr[idx]) or flag

            return flag
        return rec(start)            
