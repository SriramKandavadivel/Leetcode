# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(root):
            if not root:
                return

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

            return
        # inorder(root)
        # print(arr)
        def bst(st, end):
            if st > end:
                return None
            mid = (end + st) // 2
            root = TreeNode()
            root.val = arr[mid]
            root.left = bst(st, mid-1)
            root.right = bst(mid+1, end)

            return root

        inorder(root)
        return bst(0, len(arr)-1)
            

