class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                comp = target - nums[j]
                complement[comp] = j

                if complement.get(nums[j], 0):
                    if complement[nums[j]] != j:
                        return [complement[nums[j]], j]

                if target - nums[i] - nums[j] == 0 and i!=j:
                    return [i,j]