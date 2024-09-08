"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sv_lst = []
        hash_mapping = {}
        for idx, itm in enumerate(nums):
            
            # else:
            #     hash_mapping[itm] = idx

            if target - itm in hash_mapping:
                sv_lst.append(hash_mapping[target - itm])
                sv_lst.append(idx)
            hash_mapping[itm] = idx
        return sv_lst


if __name__ == "__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    ans = solution.twoSum(nums, target)
    print(ans)
    pass