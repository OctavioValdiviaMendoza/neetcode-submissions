class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, List<String>> anagrams = new HashMap<>();
        for(String s: strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            if(anagrams.containsKey(sorted)){
                anagrams.get(sorted).add(s);
            }
            else{
                List<String> group = new ArrayList<>();
                group.add(s);
                anagrams.put(sorted, group);
            }
        }
        for(List<String> groups: anagrams.values()){
            result.add(groups);
        }
        return result;
    }
}
