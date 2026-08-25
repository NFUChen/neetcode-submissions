class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while (left < right):
            width = (right - left)
            curr_area = width * min(heights[left], heights[right])
            max_area = max(max_area,curr_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            
        
        return max_area
