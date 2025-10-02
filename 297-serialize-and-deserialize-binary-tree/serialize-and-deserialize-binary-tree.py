# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ser = ""
        def preorder(node):
            nonlocal ser
            if not node:
                ser += "n."
                return  
            val = node.val
            print(val)
            ser += str(val) + '.'

            preorder(node.left)
            preorder(node.right)  
            
        # print(ser)
        preorder(root)
        return ser[:len(ser)-1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        d_ser = data
        #1-2-n-n-3-4-n-n-5-n-n
        l = d_ser.split('.')
        m = len(l)

        # print(l)
        idx = -1
        def build():
            nonlocal idx
            idx += 1

            # if idx >= m:
            #     return None
            if l[idx] == 'n':
                return None

            node = TreeNode()
            node.val = int( l[idx] )

            node.left = build()
            node.right = build()
            # idx += 1

            return node
        
        if l[0] == '':
            return []
        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))