from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        # 按照结束位置对区间进行排序
        points.sort(key=lambda x: x[1])
        
        merged = [points[0]]
        for i in range(1, len(points)):
            curr = points[i]
            last = merged[-1]
            if last[1] >= curr[0]:  # 如果有交集
                # 更新结束位置为交集的结束位置
                merged[-1] = [last[0], min(last[1], curr[1])]
            else:
                merged.append(curr)
                
        return len(merged)
