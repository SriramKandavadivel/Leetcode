class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length(), n = p.length();
        
        return rec(m-1,n-1,s,p);
    }

    public boolean rec(int s_idx,int p_ind, String s, String p){

        if(s_idx == -1 && p_ind == -1){
            return true;
        }

        boolean flag = false;

        if(p_ind >= 0 && s_idx >= 0 && ( p.charAt(p_ind) == '.' || s.charAt(s_idx) == p.charAt(p_ind) ) ){
            flag = flag || rec(s_idx-1, p_ind -1, s, p);
        }
        else if(p_ind >= 0 && p.charAt(p_ind) == '*' ){
            if(s_idx >= 0 && p_ind-1 >= 0){
                flag = flag || ( p.charAt(p_ind-1) == '.' || p.charAt(p_ind-1) == s.charAt(s_idx)) && rec(s_idx-1, p_ind, s, p);
            }
            // if(p_ind-2 >= 0){
            flag = flag || rec(s_idx, p_ind-2, s, p);
            // }
        }

        return flag;

    }
}