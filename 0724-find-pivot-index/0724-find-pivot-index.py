class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = sum(nums)
        
        left_sum = 0
        for j in range(n):
            right_sum = total - left_sum - nums[j]
            if left_sum == right_sum:
                return j
            left_sum += nums[j]

        return -1 