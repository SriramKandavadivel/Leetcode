/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
            // List<Integer> result = new ArrayList<>();
            // Stack<TreeNode> stack = new Stack<>();

            // while(!stack.isEmpty() || root != null){
            //     while(root != null){
            //         stack.push(root);
            //         root = root.left;
            //     }

            //     root = stack.pop();
            //     result.add(root.val);
            //     root = root.right ;
            // }
            // return result;

            return helper(root, new ArrayList<>());

    }

    public List<Integer> helper(TreeNode node, List<Integer> res){
        
        if (node == null){
            return res;
        }

        helper(node.left,res);
        res.add(node.val);
        helper(node.right,res);

        return res;

    }


}
