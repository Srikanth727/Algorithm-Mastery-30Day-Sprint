class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left = 0  
        right = n - 1
        max_area = 0
        while(left < right):
            min_h = min(height[left], height[right])
            width = right - left
            area = min_h * width
            max_area = max(max_area, area)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1   

        return max_area  
        