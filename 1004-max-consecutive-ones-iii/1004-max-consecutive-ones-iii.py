class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        zero_counter = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                zero_counter += 1
            
            if zero_counter > k:
                if nums[left] == 0:
                    zero_counter -= 1
                left += 1
            
        return n - left
            




        