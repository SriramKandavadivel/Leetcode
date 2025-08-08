class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int l = 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int r = m*n -1 ;
        if(l == r && matrix[l][r] == target) return true;
        while(l <= r){
            int mid = (l+ r)/2;
            int i = mid / n;
            int j = mid % n;
            if(matrix[i][j] == target) return true;

           else if(matrix[i][j] > target){
                r = mid-1;
            }
            else{
                l = mid+1;
            }
        }
        return false;
    }
}