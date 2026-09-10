class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0){
            return false;
        }
        boolean hasDuplicate = false;
        Set<Integer> numSet = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            numSet.add(nums[i]);
        }
        for(int j = 0; j < nums.length; j++){
            hasDuplicate = numSet.remove(nums[j]);
            if(!hasDuplicate){
                return !hasDuplicate;
            }
            
        }
        return !hasDuplicate;

    }
}