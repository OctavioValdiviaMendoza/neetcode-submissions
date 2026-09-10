class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> pair =  new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            pair.put(nums[i], i);
        }
        for(int i = 0; i < nums.length; i++){
            int temp = target;
            temp = temp - nums[i];
            if(pair.containsKey(temp) && pair.get(temp) != i){
                return new int[]{i,pair.get(temp)};
            }

        }
       return new int[]{};
    }
}
