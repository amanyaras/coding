"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""

from typing import List, Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        # 计算字符串 p 的字符计数
        p_count = Counter(p)
        # 当前窗口的字符计数
        s_count = Counter()

        result = []
        p_len = len(p)

        # 使用滑动窗口遍历字符串 s
        for i in range(len(s)):
            # 将当前字符加入窗口
            s_count[s[i]] += 1

            # 当窗口大小超过 p 的长度时，移除最左边的字符
            if i >= p_len:
                if s_count[s[i - p_len]] == 1:
                    del s_count[s[i - p_len]]
                else:
                    s_count[s[i - p_len]] -= 1

            # 如果当前窗口的字符计数和 p 的字符计数相同，则记录起始索引
            if s_count == p_count:
                result.append(i - p_len + 1)

        return result


if __name__ == "__main__":
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"
    ans = solution.findAnagrams(s, p)
    print(ans)
    pass
