class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] preArr = new int[nums.length];
        int[] postArr = new int[nums.length];
        int[] answer = new int[nums.length];

        //Array that is nums that mul before it
        for(int i = 0; i < nums.length; i++){
            if(i == 0){
                preArr[i] = 1;

            }
            else{
                preArr[i] = preArr[i-1] * nums[i-1];
            }
        }

        for(int i = nums.length - 1; i >= 0; i--){
            if(i == nums.length - 1){
                postArr[i] = 1;
            }
            else{
                postArr[i] = postArr[i + 1] * nums[i+1];
            }

        }

        for(int i = 0; i < nums.length; i++){
            answer[i] = preArr[i] * postArr[i];
        }
       
        return answer;
    }
}  
