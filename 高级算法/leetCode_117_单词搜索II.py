"""
day: 2020-08-30
url: https://leetcode-cn.com/leetbook/read/top-interview-questions-hard/xdpw1v/
题目名: 单词搜索II
给定一个二维网格board和一个字典中的单词列表words,找出所有同时在二维网格和字典中出现的单词.
单词必须按照字母顺序,通过相邻的单元格内的字母构成,其中相邻单元格是那些水平相邻或垂直相邻的单元
格.同一个单元格内的字母在一个单词中不允许被重复使用.
提示:
    你需要优化回溯算法以通过更大数据量的测试,你能否早点停止回溯?
    如果当前单词不存在于所有单词的前缀中,则可以立即停止回溯,什么样的数据结构可以有效地执行
    这样的操作?散列表是否可行?前缀树如何?
示例:
    输入: words = ['oath', 'pea', 'eat', 'rain']
          board = [
            ['o','a','a','n'],
            ['e','t','a','e'],
            ['i','h','k','r'],
            ['i','f','l','v']
          ]
    输出: ['eat', 'oath']
思路:
    利用前缀树存储单词列表words的所有单词,遍历board中的所有字符,如果有字符符合words中某个单词的开头,
    就继续深度遍历下去,直到遇到一个节点是字符串,那么将这个字符串加入结果集中,并将该节点的字符串设置为空,表示
    从树中删除该节点.
    每次深度遍历时,我们需要暂时将当前节点设置为已遍历,防止在之后的遍历重复访问同一个节点.
    在遍历结束后需要回溯该节点
"""
from typing import List


class Trie:

    def __init__(self):
        self.head = {
            'str': None,
        }

    def insert(self, word: str) -> None:
        node = self.head
        for chr in word:
            if chr not in node:
                node[chr] = {
                    'str': None,
                    'next_chars': {}
                }
            node = node[chr]
        node['str'] = word


class Solution:
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def backtrack(x, y, node):
            if node['str']:
                res.append(node['str'])
                node['str'] = None
            temp = board[x][y]
            # 将节点设置为已遍历
            board[x][y] = '$'
            for direction in self.directions:
                new_x = x + direction[0]
                new_y = y + direction[1]
                if 0 <= new_x < m and 0 <= new_y < n and board[new_x][new_y] in node:
                    backtrack(new_x, new_y, node[board[new_x][new_y]])
            # 回溯
            board[x][y] = temp
        m = len(board)
        if not m or not words:
            return []
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.head:
                    backtrack(i, j, trie.head[board[i][j]])
        return res


if __name__ == "__main__":
    test = ['aaa']
    test2 = [
        ['a', 'a']
    ]
    s = Solution()
    print(s.findWords(test2, test))
