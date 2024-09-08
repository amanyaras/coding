"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        max_len = 0
        for itm in nums:
            tmp = 0
            if itm - 1 in nums:
                continue
            while itm in nums:
                itm += 1
                tmp += 1
            max_len = max(max_len, tmp)
        return max_len

if __name__ == '__main__':
    nums = [100,4,200,1,3,2]
    solution = Solution()
    ans = solution.longestConsecutive(nums)
    print(ans)
    pass