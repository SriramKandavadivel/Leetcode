# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = collections.defaultdict(lambda: collections.defaultdict(list))
        ans = []

        def rec(root,row,col):
            if not root:
                return 
            d[col][row].append(root.val)
            rec(root.left,row+1,col-1)
            rec(root.right,row+1,col+1)
        
        rec(root,0,0)
        print(d)
        for col_key in sorted(d.keys()):
            l = []
            for row_key in sorted(d[col_key].keys()):
                for val in sorted(d[col_key][row_key]):
                    l.append(val)
            ans.append(l)
        
        return ans