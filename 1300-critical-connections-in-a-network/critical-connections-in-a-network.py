class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dis = collections.defaultdict(list)   #discovery
        ls_dis = collections.defaultdict(list)  #least disc
        d_t = 0                            #disc time
        l_t = 0                            #least dic time
        gf = collections.defaultdict(list)  #graph
        for x,y in connections:
            gf[x].append(y)                #as given graph is undirected we will connect both ways
            gf[y].append(x)
        # print(gf)
        vis = [False]*n
        ans =[]
        def neigh(node,parent):
            nonlocal d_t,l_t
            d_t += 1
            l_t += 1
            ls_dis[node] = l_t
            dis[node] = d_t
            vis[node] = True
            for i in range(len(gf[node])):
                des = gf[node][i]
                if des == parent:
                    continue
                elif vis[des]:
                    ls_dis[node] = min(ls_dis[node], dis[des])
                elif not vis[des]:
                    neigh(des,node)
                    ls_dis[node] = min(ls_dis[node], ls_dis[des])
                    if dis[node] < ls_dis[des]:
                        ans.append([node,des])
        neigh(0,-1)
        return ans