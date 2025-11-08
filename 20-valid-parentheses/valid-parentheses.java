class Solution {
    public boolean isValid(String s) {
        Stack<Character> s1 = new Stack<>();
        Stack<Character> s2 = new Stack<>();
        if (s == null) {
            return true;
        }
        if(s.length() == 1)
        return false;
        for (int i = 0; i < s.length(); i++) {
            char p = s.charAt(i);
            // if (s.length() == 1)
            //     return false;
            if (p == '{' || p == '(' || p == '[') {
                s1.push(p);
            }

                if (p == '}' || p == ')' || p == ']') {
                    if (s1.isEmpty())
                        return false;
                    else if ((p == '}' && s1.pop() == '{'))
                        continue;
                    else if (p == ']' && s1.pop() == '[')
                        continue;
                    else if (p == ')' && s1.pop() == '(')
                        continue;
                    else
                        return false;
                
            }

        }
        if(s1.isEmpty())
            return true;
        return false;

    }
}