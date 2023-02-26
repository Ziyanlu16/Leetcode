package Leetcode;

class Solution {
    public int wiggleMaxLength(int[] nums) {
        int n = nums.length;
        if (n < 2) {
            return n;
        }
        int i = 1;
        while (i < n && nums[i] == nums[i-1]) {
            i++;
        }
        if (i == n) {
            return 1;
        }
        int start = nums[i] - nums[i-1];
        int max_length = 2;
        for (i = i+1; i < n; i++) {
            int diff = nums[i] - nums[i-1];
            if ((diff > 0 && start <= 0) || (diff < 0 && start >= 0)) {
                max_length++;
                start = diff;
            }
        }
        return max_length;
    }
}
