class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return len(set(nums)) < len(nums) 
        d = set()
        for x in nums:
            if x in d:
                return True
            d.add(x)
        return False