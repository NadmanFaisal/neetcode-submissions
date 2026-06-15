class Solution {
    public boolean isAnagram(String s, String t) {        
        if(s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> countS = new HashMap<>();
        HashMap<Character, Integer> countT = new HashMap<>();

        for(int i = 0; i < s.length(); i++) {
            int sCount = countS.containsKey(s.charAt(i)) ? countS.get(s.charAt(i)) : 0;
            countS.put(s.charAt(i), sCount + 1);

            int tCount = countT.containsKey(t.charAt(i)) ? countT.get(t.charAt(i)) : 0;
            countT.put(t.charAt(i), tCount + 1);
        }

        return countS.equals(countT);
    }
}
