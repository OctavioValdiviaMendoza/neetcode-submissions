class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<>();
        for(int num: nums){
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        List<Map.Entry<Integer,Integer>> entries = new ArrayList<>(count.entrySet());
        entries.sort((a,b)-> Integer.compare(b.getValue(),a.getValue()));

        int[] answer = new int[k];
        for(int i = 0; i < k; i++){
            answer[i] = (entries.get(i).getKey());
        }
        return answer;
    }
}