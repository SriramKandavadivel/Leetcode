class Solution {
    public int titleToNumber(String columnTitle) {
        int res = 0;
        for(char c : columnTitle.toCharArray()){
            res = res * 26 + Character.valueOf(c) - 64;
        }
        return res;
    }
}