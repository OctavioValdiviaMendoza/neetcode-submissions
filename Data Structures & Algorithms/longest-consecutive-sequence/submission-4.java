class Solution {
    public int longestConsecutive(int[] nums) {
        int max = 0;
        int sequence = 1;
        Set<Integer> numSet = new HashSet<>();
        for(int x: nums){
            numSet.add(x);
        }

        for(int i = 0; i < nums.length; i++){
            if(!numSet.contains(nums[i] - 1)){
                int j = 1;
                while(numSet.contains(nums[i] + j)){
                    sequence += 1;
                    j += 1;
                }
                if(sequence > max){
                    max = sequence;
                }
                sequence = 1;
            }
        }
        return max;

    }
}
