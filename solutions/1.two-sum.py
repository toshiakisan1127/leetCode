#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(N^2) solution
        # nums_length = len(nums)
        # ans = []
        # for i in range(nums_length):
        #     for j in range(i+1, nums_length):
        #         if nums[i] + nums[j] == target:
        #             ans.append(i)
        #             ans.append(j)
        #             return ans

        # O(N) solution
        hash_map: Dict = {num: i for i, num in enumerate(nums)}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in hash_map and hash_map[difference] != i:
                return [i, hash_map[difference]]

# @lc code=end
