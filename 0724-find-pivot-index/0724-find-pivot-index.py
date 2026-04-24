class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
        
        left_sum = 0
        for j in range(n):
            right_sum = total - left_sum - nums[j]
            if left_sum == right_sum:
                return j
            left_sum += nums[j]

        return -1 