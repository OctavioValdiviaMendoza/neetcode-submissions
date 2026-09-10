class Solution {
    public int[] countBits(int n) {
        int[] arr = new int[n + 1];
        arr[0] = 0;
        for(int i = 1; i <= n; i++){
            int temp = i;
            int counter = 0;
            while(temp != 0){
                counter += temp % 2;
                temp >>>= 1;         
            }
            arr[i] = counter;
        }
        return arr;
        
    }
}
