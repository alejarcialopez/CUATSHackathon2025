class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for x in nums:
            if curSum < 0:
                curSum = 0
            curSum += x
            if maxSum < curSum:
                maxSum = curSum
        return maxSum