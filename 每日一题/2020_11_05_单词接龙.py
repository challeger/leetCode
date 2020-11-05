"""
day: 2020-11-05
url: https://leetcode-cn.com/problems/word-ladder/
题目名: 单词接龙
给定两个单词(beginWord和endWord)和一个字典,找到从beginWord到endWord的最短
转换序列的长度,转换需遵循如下规则:
    每次转换只能改变一个字母。
    转换过程中的中间单词必须是字典中的单词。

说明:

    如果不存在这样的转换序列，返回 0。
    所有单词具有相同的长度。
    所有单词只由小写字母组成。
    字典中不存在重复的单词。
    你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例1:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    输出: 5


思路:
双向bfs
"""
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)  # 转为集合对象,查询的时间复杂度为O(1)
        # 如果没有单词,或者结束的单词不在集合中,那么是没有结果的
        if not len(word_set) or endWord not in word_set:
            return 0

        visited = set((beginWord, endWord))  # 记录已经走过的单词

        left_visited = set()
        left_visited.add(beginWord)
        right_visited = set()
        right_visited.add(endWord)

        word_len = len(beginWord)  # 单词的长度
        step = 1
        while left_visited:
            # 保证每次都是找最少的单词
            if len(left_visited) > len(right_visited):
                left_visited, right_visited = right_visited, left_visited

            next_level = set()  # 下一层的单词数
            for word in left_visited:
                word_list = list(word)  # 转为列表,才能进行替换
                for i in range(word_len):
                    origin_char = word_list[i]  # 原本的字符
                    for j in range(26):
                        word_list[i] = chr(97 + j)  # 每个字符都尝试一次
                        next_word = ''.join(word_list)  # 拼接回字符串

                        if next_word in word_set:  # 判断单词是否在列表中
                            if next_word in right_visited:  # 如果在右边的已经访问过的单词中,那么就说明可以到达
                                return step + 1  # 加1是因为还需要1步才能到下一层
                            if next_word not in visited:  # 没有访问过,就添加到下一层要访问的序列中
                                next_level.add(next_word)
                                visited.add(next_word)
                    word_list[i] = origin_char
            left_visited = next_level
            step += 1
        return 0
