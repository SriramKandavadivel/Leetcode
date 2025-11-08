class Solution {
    public String decodeString(String s) {
        Stack<Integer> count = new Stack<>();
        Stack<StringBuilder> strStack = new Stack<>();

        StringBuilder sb = new StringBuilder();
        int n = 0;
        for(char c : s.toCharArray()){
            if(Character.isDigit(c)){
                n = n*10 + (c-'0');
            }
            else if( c == '['){
                count.push(n);
                n = 0;
                strStack.push(sb);
                sb = new StringBuilder();
            }
            else if(c == ']'){
                int k = count.pop();
                StringBuilder prev = strStack.pop();
                // StringBuilder x = sb;
                // sb = strStack.pop();
                for(int i = 0; i < k; i++){
                    prev.append(sb);
                }
                sb = prev;
            }
            else{
                sb.append(c);
            }
        }
        return sb.toString();
    }
}