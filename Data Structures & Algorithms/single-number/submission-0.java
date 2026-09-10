class Solution {
    public int singleNumber(int[] nums) {
        int starter = nums[0];
        for(int i = 1; i < nums.length; i++){
            starter = starter ^ nums[i];
        }
        
        return starter;

        
    }
}
