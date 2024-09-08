"""

给定一个字符串 s ，请你找出其中不含有重复字符的 最长 
子串的长度。

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
"""
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。

s = "abcabcbb"
# print(s[3])
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希集合，用于存储当前窗口中的字符
        char_set = set()
        # 左指针初始化为 0
        left = 0
        # 记录最长子串长度
        max_len = 0
        
        # 右指针从 0 开始遍历
        for right in range(len(s)):
            # 如果字符 s[right] 在集合中，则移动左指针直到 s[right] 不在集合中
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            # 将 s[right] 加入集合
            char_set.add(s[right])
            # 更新最大长度
            max_len = max(max_len, right - left + 1)
        
        return max_len



if __name__ == "__main__":
    solution = Solution()
    ans = solution.lengthOfLongestSubstring(s)
    print(ans)