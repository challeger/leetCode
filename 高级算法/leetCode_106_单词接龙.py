"""
day: 2020-08-27
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xwjmmm/
题目名: 单词接龙
给定两个单词(beginWord和endWord)和一个字典,找到beginWord和endWord的最短转换序列的长度.
转换需要遵循如下规则:
    1.每次转换只能改变一个字母
    2.转换过程中的中间单词必须是字典中的单词
说明:
    1.如果不存在这样的转换序列,返回0
    2.所有单词具有相同的长度,且只由小写字母组成
    3.字典中不存在重复的单词
    4.可以假设beginWord和endWord是非空的,且二者不相同
示例:
    输入: beginWord='hit',endWord='cog',wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    输出: 5
    解释: hit->hot->dot->dog->cog
思路:
1. 图&广度优先遍历
    图是一种非线性的关系型数据结构,对于本题,如果两个单词能够修改一个字符就相等,那么他们就是相连的.
    通过广度优先遍历,我们就可以得到最短的转换序列的长度

    如何建图?:
        我们使用队列,在一开始先将beginWord加入队列中,然后依次将26个字符与beginWord中的字符替换,若替换
        后得到的单词在wordList中,那么就添加到队列里,也就是我们下一层要访问的节点..
        为了避免环,我们需要增加一个visited集合,来记录我们访问过的单词,在对比时,依次出队
        如果单词在list中,我们还需判断是否在visited中,若不在的话再添加到队列与visited集合中..
    何时结束?:
        当我们在某一次字符替换,得到的单词是endWord时,返回结果,
        若遍历完成都没得到,则返回0
2. 双向广度优先
    双向广度优先就是依次从开始和结束的节点进行广度优先遍历,因为开始的节点只有一个,结束的节点也只有一个.
    如果我们单向遍历,在到达结束的前一层,其实会有很多无用的单词对比,若我们双向遍历,我们只需判断本次遍历的
    单词,是否在另一层被访问过,如果被访问过,说明下一次遍历就会相遇,那么路线就连接起来了,这时就可以返回结果了

    我们在每次广度遍历时,选择两边单词数较小的一边进行扩散
"""
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # # 将列表中的所有单词保存在哈希表中,以此实现O(1)的查找
        # wordSet = set(wordList)
        # # 特判
        # if not len(wordSet) or endWord not in wordSet:
        #     return 0

        # # 队列,先进先出,后进后出,用来实现bfs
        # queue = deque()
        # # 开始的单词为第一层
        # queue.append(beginWord)
        # # 访问过的数组,避免图中的环
        # visited = set()
        # visited.add(beginWord)

        # # 每次循环都要依次替换单词中的各个单词,所以需要单词的长度
        # word_len = len(beginWord)
        # # 开始到结束至少要一步
        # step = 1
        # while queue:
        #     # 当前层的节点数量
        #     current_size = len(queue)
        #     for i in range(current_size):
        #         # 弹出队首元素
        #         word = queue.popleft()
        #         # 将单词转换为列表,才能修改
        #         word_list = list(word)
        #         for j in range(word_len):
        #             # 记录原本的字符
        #             origin_char = word_list[j]

        #             # 依次替换26个字母
        #             for k in range(26):
        #                 word_list[j] = chr(ord('a') + k)
        #                 next_word = ''.join(word_list)
        #                 # 如果单词在单词列表中
        #                 if next_word in wordSet:
        #                     # 如果是目标单词,那么返回结果
        #                     if next_word == endWord:
        #                         return step + 1
        #                     # 否则判断是否访问过该单词.若没访问过则
        #                     if next_word not in visited:
        #                         # 将该单词添加到下一层要访问的队列中
        #                         queue.append(next_word)
        #                         # 将单词设置为已访问
        #                         visited.add(next_word)
        #             # 将单词恢复
        #             word_list[j] = origin_char
        #     # 每进一层步长+1
        #     step += 1
        # return 0
        wordSet = set(wordList)
        # 特判
        if not len(wordSet) or endWord not in wordSet:
            return 0
        visited = set()
        visited.add(beginWord)
        visited.add(endWord)

        start_visited = set()
        start_visited.add(beginWord)

        end_visited = set()
        end_visited.add(endWord)

        word_len = len(beginWord)
        step = 1
        while start_visited:
            # 每次都搜索单词量较少的一层.
            if len(start_visited) > len(end_visited):
                start_visited, end_visited = end_visited, start_visited

            next_level = set()
            for word in start_visited:
                word_list = list(word)
                for i in range(word_len):
                    origin_char = word_list[i]
                    for j in range(26):
                        word_list[i] = chr(ord('a') + j)
                        next_word = ''.join(word_list)
                        if next_word in wordSet:
                            # 如果单词在另一边已经访问过,说明在下一次遍历两边就会相遇
                            # 那么返回结果
                            if next_word in end_visited:
                                return step + 1
                            # 否则判断单词是否已经访问过
                            if next_word not in visited:
                                # 没有就加到本边的访问过的单词里
                                next_level.add(next_word)
                                visited.add(next_word)
                    word_list[i] = origin_char
            # 访问下一层
            start_visited = next_level
            step += 1
        return 0


if __name__ == "__main__":
    begin = 'hit'
    end = 'cog'
    test = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
    s = Solution()
    print(s.ladderLength(begin, end, test))
