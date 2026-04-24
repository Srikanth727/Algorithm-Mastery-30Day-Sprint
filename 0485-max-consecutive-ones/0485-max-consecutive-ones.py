class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = 0
        window_sum = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                window_sum += nums[i]
            
            else:
                max_sum = max(max_sum, window_sum)
                window_sum = 0
                continue
        
        return max(max_sum, window_sum)