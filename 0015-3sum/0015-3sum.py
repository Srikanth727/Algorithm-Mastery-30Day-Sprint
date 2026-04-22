class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l_nums = len(nums)
        solution = set()
        first = 0
        while first < l_nums - 2:
            left = first + 1
            right = l_nums - 1
            while left < right:
                total = nums[left] + nums[right]
                if (nums[first] + total) == 0:
                    solution.add((nums[first], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif (nums[first] + total) > 0:
                    right -= 1
                else:
                    left += 1
            first += 1

        return [list(triplet) for triplet in solution]
