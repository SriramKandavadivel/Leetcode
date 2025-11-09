class Solution {
    public Boolean[][] cache;
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        cache = new Boolean[m+1][n+1];

        return rec(m-1,n-1, s, p);
    }

    public boolean rec(int idx, int ind, String s, String p){
        
        if(idx == -1 && ind == -1){
            return true;
        }
        if( cache[idx+1][ind+1] != null){
            return cache[idx+1][ind+1] ;
        }
        boolean best = false;

        if( idx >= 0 && ind >= 0 && (p.charAt(ind) == '?' || s.charAt(idx) == p.charAt(ind)) ){
            best = best || rec(idx-1, ind-1, s, p);
        }
        else if( ind >= 0 && p.charAt(ind) == '*' ){
            if( idx >= 0 ){
                best = best || rec(idx-1, ind, s, p);
            }

            best = best || rec( idx, ind-1, s, p);
        }
        cache[idx+1][ind+1] = best;
        return best;
    }
}