from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset= [[]]
        for n in nums:
            powerset += [[n] +  p for p in powerset]
        return powerset

# start pst = [[]] 
#  add to each set in pst 1 but copy over last pst. pst = [[], [1]]
#  add to each set in pst 2 but copy over last pst. pst = [[], [1], [2], [1,2]]