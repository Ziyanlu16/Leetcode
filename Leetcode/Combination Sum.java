import java.util.*;

class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<>();
        backtrack(candidates, target, 0, 0, new ArrayList<>(), result);
        return result;
    }
    
    private void backtrack(int[] candidates, int target, int start, int currSum, List<Integer> currList, List<List<Integer>> result) {
        if (currSum == target) {
          result.add(new ArrayList<>(currList));
          return;
        }
        if (currSum > target) {
          return;
        }
  
        for (int i = start; i < candidates.length; i++) {
          currList.add(candidates[i]);
          backtrack(candidates, target, i, currSum + candidates[i], currList, result);
          currList.remove(currList.size() - 1);
        }
    }
  }
  