class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean valid = false;
        int j = 0;
        
        for(int i = 0; i < nums.length - 1; i++) {
            for(j = i + 1; j < nums.length; j++) {
                if(nums[i] == nums[j]) {
                    return true;
                }
            }
        }

        return false;
    }
}
