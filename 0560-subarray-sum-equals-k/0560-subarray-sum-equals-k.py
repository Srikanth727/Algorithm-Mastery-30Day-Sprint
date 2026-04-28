class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        currSum = 0
        count = 0
        prefixSum = {0 : 1}

        for i in range(len(nums)):
            currSum += nums[i]
            diff = currSum - k
            count += prefixSum.get(diff, 0)
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
        
        return count
        