"""
day: 2020-08-17
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-medium/xvaszc/
题目名: 字母异位词分组
题目描述: 给定一个字符串数组,将字母异位词组合在一起,字母异位词指字母相同但排列不同的字符串
示例:
    输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
    输出:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
思路:
1.以排序后的字符串为键
    字符串列表为值,遍历strs,每次将字符串append进对应的列表中
    最终返回字典的values
2, 以字符出现的次数为键
    字符串列表为值,遍历strs,记录每个str中字符出现的次数,以此为
    键将字符串添加到对应的列表中
"""


class Solution:
    def groupAnagrams(self, strs: list) -> list:
        import collections
        ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


if __name__ == "__main__":
    test = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(test))
