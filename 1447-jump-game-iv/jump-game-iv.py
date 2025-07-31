class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        INF = 10**20
        same_lookup = collections.defaultdict(list)
        for i in range(n):
            same_lookup[arr[i]].append(i)
        q = deque([(0,0)])  ## jump,index
        ans = [INF]*n
        visited_sameval = set()
        ans[0] = 0
        while q:
            jumps,idx = q.popleft()
            for x in [idx-1,idx+1]:
                if 0 <= x < n and ans[x] > jumps+1:
                    ans[x] = jumps+1
                    q.append([ans[x],x])
            if arr[idx] not in visited_sameval:
                visited_sameval.add(arr[idx])

                for j in same_lookup[arr[idx]]:
                    if j != idx and ans[j] > jumps+1:
                        ans[j] = jumps+1
                        q.append([ans[j],j])
                    
        return ans[-1] if ans[-1] != INF else -1

