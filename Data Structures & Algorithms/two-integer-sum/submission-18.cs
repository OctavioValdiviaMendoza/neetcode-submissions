public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = i + 1; j < nums.Length; j++)
            {
                if (nums[i] + nums[j] == target)
                {
                    int[] arr = {i,j};
                    return arr;
                }
            }
        }
        int[] arr2 = {0,0};
        return arr2;

    }
}
