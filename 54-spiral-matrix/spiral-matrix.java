class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        List<Integer> res = new ArrayList<>();
        
        int left = 0, right = n-1;
        int top = 0, bot = m-1;
        
        while(top <= bot && left <= right){
            for(int i = left; i <= right; i++){
                res.add( matrix[top][i] );
            }
            top++;

            for(int j = top; j <= bot; j++){
                res.add( matrix[j][right] );
            }
            right--;
            if(top <= bot){
                for(int i = right; i >= left; i--){
                    res.add( matrix[bot][i] );
                }
                bot--;
            }
            
            if(left <= right){
                for(int j = bot; j >= top; j--){
                    res.add( matrix[j][left] );
                }
                left++;
            }
        }

        return res;
    }
}