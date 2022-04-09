from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """

        """
        # O(N^2)
        ans = []
        nums_length = len(nums)
        for i in range(0, nums_length):
            for j in range(i, nums_length):
                if nums_length[i] + nums_length[j] == target:
                    ans.append(i)
                    ans.append(j)
                    break
            else:
                continue
            break

        return ans
