class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String> > h1 = new HashMap<>();

        for(String s : strs){
            char[] d = s.toCharArray();
            Arrays.sort(d);
            String h_val = new String(d);

            if( h1.containsKey(h_val)){
                // h1.put( h_val, h1.get(h_val).add(s));
                h1.get(h_val).add(s);
            }
            else{
                List<String> newList = new ArrayList<>();
                newList.add(s);
                h1.put( h_val, newList );
            }
        }

        List<List<String>> res = new ArrayList<>(h1.values());

        return res;
    }
}