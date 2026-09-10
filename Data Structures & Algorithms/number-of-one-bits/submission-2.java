class Solution {
    public int hammingWeight(int n) {
        int counter = 0;
        while(n != 0){
           counter += n % 2;
           n >>>= 1;
        }

        return counter;
    }
}
