class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        # n = len(edges)
        cnt = 0

        for x in edges:
            n1 = x[0]
            n2 = x[1]

            d[n1].append(n2)
            d[n2].append(n1)

        vis = set()
        set2 = set()
        set3 = set()
        def dfs(node):
            nonlocal cnt
            vis.add(node)
            set2.add(node)
            set3.add( len(d[node]))
            for x in d[node]:
                if x not in vis:
                    dfs(x)
            
            

            return


        for i in range(n):
            if i not in vis:
                dfs(i)
                c = len(set2)
                set2 = set()
                if len(set3) == 1 and c-1 in set3 :
                    cnt += 1
                set3 = set()
        
        return cnt