class Solution {
    public int maxArea(int[] height) {
        int Maxarea = Integer.MIN_VALUE;
        int low = 0;
        int high = height.length - 1;
        while (low < high) {
          int shortline = Math.min(height[low], height[high]);
          Maxarea = Math.max(Maxarea, shortline * (high - low));
          if (height[low] > height[high]) {
            high--;
          }else{
            low++;
          }
        }
        return Maxarea;
    }
  }