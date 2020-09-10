"""
day: 2020-09-10
url: https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii/
题目名: 替换和查找模式
你有一个单词列表 words 和一个模式  pattern,你想知道 words 中的哪些单词与模式匹配。
如果存在字母的排列 p ,使得将模式中的每个字母 x 替换为 p(x) 之后,我们就得到了所需的单词,那么单词与模式是匹配的。
（回想一下,字母的排列是从字母到字母的双射：每个字母映射到另一个字母,没有两个字母映射到同一个字母。）
返回 words 中与给定模式匹配的单词列表。
你可以按任何顺序返回答案。
示例:
    输入: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
    输出: ["mee","aqq"]
思路:
    一个字典记录当前的映射关系,一个集合记录已经映射的值

    如果word中的某个字母已经建立了映射关系,但当前pattern的字母与其不相等, false
    如果word中的某个字母未建立映射关系, 但当前pattern的字母已经建立映射关系, false
    如果遍历完成,添加到结果中
"""


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            hashmap = {}
            values = set()
            for i in range(len(word)):
                if word[i] in hashmap:
                    if hashmap[word[i]] != pattern[i]:
                        break
                else:
                    if pattern[i] in values:
                        break
                    hashmap[word[i]] = pattern[i]
                    values.add(pattern[i])
            else:
                ans.append(word)
        return ans
