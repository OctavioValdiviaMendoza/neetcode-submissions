class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){ 
            return false;
        }
        Map<Character, Integer> letterCountS = new HashMap<>();
        Map<Character, Integer> letterCountT = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            letterCountS.put(s.charAt(i),letterCountS.getOrDefault(s.charAt(i),0) + 1);
        }
        for(int j = 0; j < t.length(); j++){
            letterCountT.put(t.charAt(j), letterCountT.getOrDefault(t.charAt(j),0) + 1);
        }
        
        return letterCountS.equals(letterCountT);

    }
}
