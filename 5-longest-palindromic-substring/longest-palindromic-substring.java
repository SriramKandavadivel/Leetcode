class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        String res = "", odd, even;
        for(int i = 0; i < n; i++){
            even = isPal(i,i,s,n);
            odd = isPal(i, i+1,s,n);

            if (odd.length() > res.length()){
                res = odd;
            }
            if(even.length() > res.length()){
                res = even;
            }
        }
        return res;
    }
    public String isPal(int l, int r, String s, int n){

        while(l >= 0 && r < n && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }

        return s.substring(l+1,r);
    }
}