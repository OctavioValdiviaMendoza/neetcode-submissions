class Solution {
    int max = 0;
    int temp = 0;
    Set<Integer> allNums = new HashSet<>();
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        for(int num: nums){
            allNums.add(num);
        }
       for(int i = 0; i < nums.length; i++){
            checkIfContain(nums[i]);
       }

        max += 1;
        return max;
        
    }

    public void checkIfContain(int num){
        if(allNums.contains(num - 1)){
            temp += 1;
            checkIfContain(num - 1);
        }
        else{
            if(temp > max){
                max = temp;
                temp = 0;
            }
            temp = 0;
        }
        
    }
}
