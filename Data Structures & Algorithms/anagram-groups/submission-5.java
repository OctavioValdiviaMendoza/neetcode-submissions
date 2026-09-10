class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> result = new HashMap<>();
        for(String s: strs){
            char[] charArr = s.toCharArray();
            Arrays.sort(charArr);
            String sorted = new String(charArr);
            result.putIfAbsent(sorted, new ArrayList<>());
            result.get(sorted).add(s);
        }
        return new ArrayList<>(result.values());
    }
}
